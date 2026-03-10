// Web-compatible database fallback using localStorage
// Metro bundler picks this file automatically for web builds

const STORAGE_KEY = 'lifepro_db';

interface DB {
  habits: any[];
  habit_completions: any[];
  mood_entries: any[];
  sleep_entries: any[];
  water_entries: any[];
  transactions: any[];
  savings_goals: any[];
}

function loadDb(): DB {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return JSON.parse(raw);
  } catch {}
  return {
    habits: [],
    habit_completions: [],
    mood_entries: [],
    sleep_entries: [],
    water_entries: [],
    transactions: [],
    savings_goals: [],
  };
}

function saveDb(db: DB): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(db));
}

function now(): string {
  return new Date().toISOString().replace('T', ' ').slice(0, 19);
}

// === Habit Queries ===

export async function getAllHabits(): Promise<any[]> {
  const db = loadDb();
  return db.habits
    .filter((h) => !h.is_archived)
    .sort((a, b) => a.sort_order - b.sort_order || a.created_at.localeCompare(b.created_at));
}

export async function insertHabit(habit: {
  id: string;
  name: string;
  icon: string;
  color: string;
  frequency: string;
  frequencyDays: string | null;
  reminderTime: string | null;
  category: string;
  sortOrder: number;
}): Promise<void> {
  const db = loadDb();
  db.habits.push({
    id: habit.id,
    name: habit.name,
    icon: habit.icon,
    color: habit.color,
    frequency: habit.frequency,
    frequency_days: habit.frequencyDays,
    reminder_time: habit.reminderTime,
    category: habit.category,
    sort_order: habit.sortOrder,
    is_archived: 0,
    created_at: now(),
    updated_at: now(),
  });
  saveDb(db);
}

export async function updateHabitDb(id: string, updates: Record<string, any>): Promise<void> {
  const db = loadDb();
  const idx = db.habits.findIndex((h) => h.id === id);
  if (idx !== -1) {
    Object.assign(db.habits[idx], updates, { updated_at: now() });
    saveDb(db);
  }
}

export async function deleteHabitDb(id: string): Promise<void> {
  const db = loadDb();
  db.habits = db.habits.filter((h) => h.id !== id);
  db.habit_completions = db.habit_completions.filter((c) => c.habit_id !== id);
  saveDb(db);
}

// === Completion Queries ===

export async function getCompletionsForHabit(habitId: string): Promise<string[]> {
  const db = loadDb();
  return db.habit_completions
    .filter((c) => c.habit_id === habitId)
    .sort((a, b) => b.completed_date.localeCompare(a.completed_date))
    .map((c) => c.completed_date);
}

export async function getCompletionsForDate(date: string): Promise<{ habit_id: string }[]> {
  const db = loadDb();
  return db.habit_completions
    .filter((c) => c.completed_date === date)
    .map((c) => ({ habit_id: c.habit_id }));
}

export async function toggleCompletionDb(
  id: string,
  habitId: string,
  date: string
): Promise<boolean> {
  const db = loadDb();
  const idx = db.habit_completions.findIndex(
    (c) => c.habit_id === habitId && c.completed_date === date
  );

  if (idx !== -1) {
    db.habit_completions.splice(idx, 1);
    saveDb(db);
    return false;
  } else {
    db.habit_completions.push({
      id,
      habit_id: habitId,
      completed_date: date,
      completed_at: now(),
    });
    saveDb(db);
    return true;
  }
}

// === Mood Queries ===

export async function getMoodForDate(date: string): Promise<any | null> {
  const db = loadDb();
  return db.mood_entries.find((m) => m.date === date) || null;
}

export async function upsertMood(
  id: string,
  date: string,
  score: number,
  tags: string[]
): Promise<void> {
  const db = loadDb();
  const idx = db.mood_entries.findIndex((m) => m.date === date);
  const entry = { id, date, score, tags: JSON.stringify(tags), created_at: now() };
  if (idx !== -1) {
    db.mood_entries[idx] = { ...db.mood_entries[idx], score, tags: JSON.stringify(tags) };
  } else {
    db.mood_entries.push(entry);
  }
  saveDb(db);
}

export async function getMoodHistory(limit: number = 30): Promise<any[]> {
  const db = loadDb();
  return db.mood_entries
    .sort((a, b) => b.date.localeCompare(a.date))
    .slice(0, limit);
}

// === Sleep Queries ===

export async function getSleepForDate(date: string): Promise<any | null> {
  const db = loadDb();
  return db.sleep_entries.find((s) => s.date === date) || null;
}

export async function upsertSleep(
  id: string,
  date: string,
  hours: number,
  quality: number
): Promise<void> {
  const db = loadDb();
  const idx = db.sleep_entries.findIndex((s) => s.date === date);
  const entry = { id, date, hours, quality, created_at: now() };
  if (idx !== -1) {
    db.sleep_entries[idx] = { ...db.sleep_entries[idx], hours, quality };
  } else {
    db.sleep_entries.push(entry);
  }
  saveDb(db);
}

// === Water Queries ===

export async function getWaterForDate(date: string): Promise<any | null> {
  const db = loadDb();
  return db.water_entries.find((w) => w.date === date) || null;
}

export async function upsertWater(
  id: string,
  date: string,
  glasses: number
): Promise<void> {
  const db = loadDb();
  const idx = db.water_entries.findIndex((w) => w.date === date);
  if (idx !== -1) {
    db.water_entries[idx] = { ...db.water_entries[idx], glasses };
  } else {
    db.water_entries.push({ id, date, glasses, target: 8, created_at: now() });
  }
  saveDb(db);
}

// === Transaction Queries ===

export async function getTransactionsForMonth(yearMonth: string): Promise<any[]> {
  const db = loadDb();
  return db.transactions
    .filter((t) => t.date.startsWith(yearMonth))
    .sort((a, b) => b.date.localeCompare(a.date));
}

export async function insertTransaction(tx: {
  id: string;
  amount: number;
  category: string;
  description: string;
  type: string;
  date: string;
}): Promise<void> {
  const db = loadDb();
  db.transactions.push({ ...tx, created_at: now() });
  saveDb(db);
}

export async function deleteTransactionDb(id: string): Promise<void> {
  const db = loadDb();
  db.transactions = db.transactions.filter((t) => t.id !== id);
  saveDb(db);
}

// === Savings Goals Queries ===

export async function getAllSavingsGoals(): Promise<any[]> {
  const db = loadDb();
  return db.savings_goals.sort((a, b) => b.created_at.localeCompare(a.created_at));
}

export async function insertSavingsGoal(goal: {
  id: string;
  name: string;
  targetAmount: number;
}): Promise<void> {
  const db = loadDb();
  db.savings_goals.push({
    id: goal.id,
    name: goal.name,
    target_amount: goal.targetAmount,
    current_amount: 0,
    created_at: now(),
  });
  saveDb(db);
}

export async function updateSavingsGoalAmount(id: string, amount: number): Promise<void> {
  const db = loadDb();
  const idx = db.savings_goals.findIndex((g) => g.id === id);
  if (idx !== -1) {
    db.savings_goals[idx].current_amount = amount;
    saveDb(db);
  }
}

// Unused on web, but exported for compatibility
export async function getDatabase(): Promise<any> {
  return {};
}
