# 🏗 Architecture Documentation
Overview
Deriverse Dashboard is a modern web application built with Next.js 15 (App Router), React 18, and TypeScript. This document provides a detailed overview of the system architecture, design decisions, and implementation patterns.

Table of Contents
System Architecture
Directory Structure
Component Architecture
Data Layer
State Management
Styling Architecture
Error Handling
Testing Strategy
Performance Considerations
Security Measures
1. System Architecture
High-Level Architecture
┌─────────────────────────────────────────────────────────────────┐
│                        Client Browser                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    Next.js App Router                      │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                 Layout (layout.tsx)                  │  │  │
│  │  │  ┌─────────────────────────────────────────────┐    │  │  │
│  │  │  │              Context Providers               │    │  │  │
│  │  │  │  • ThemeProvider (Dark/Light Mode)          │    │  │  │
│  │  │  │  • ErrorBoundary (Error Handling)           │    │  │  │
│  │  │  └─────────────────────────────────────────────┘    │  │  │
│  │  │                        │                             │  │  │
│  │  │  ┌─────────────────────┴─────────────────────────┐  │  │  │
│  │  │  │                 Page Components               │  │  │  │
│  │  │  │  • Dashboard (/)                              │  │  │  │
│  │  │  │  • Portfolio (/portfolio)                     │  │  │  │
│  │  │  │  • Analysis (/advanced)                       │  │  │  │
│  │  │  │  • Journal (/journal)                         │  │  │  │
│  │  │  └───────────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                         Data Layer                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │   Mock Data     │  │    Utilities    │  │   Type Defs     │  │
│  │  (mock-data.ts) │  │   (utils.ts)    │  │   (types.ts)    │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
Technology Stack
Layer	Technology	Version	Purpose
Framework	Next.js	15.1.0	Server-side rendering, routing
UI Library	React	18.2.0	Component-based UI
Language	TypeScript	5.9	Type safety
Styling	Tailwind CSS	4.1	Utility-first CSS
Charts	Recharts	2.15	Data visualization
Icons	Lucide React	0.400	Icon library
Testing	Jest	30.2	Unit testing
2. Directory Structure
Directory Tree
deriverse-dashboard/
│
├── app/                              # Next.js App Router
│   ├── layout.tsx                    # Root layout
│   ├── page.tsx                      # Home page
│   ├── globals.css                   # Global styles
│   ├── advanced/page.tsx             # Analysis page
│   ├── journal/page.tsx              # Journal page
│   └── portfolio/page.tsx            # Portfolio page
│
├── components/                       # React Components
│   ├── analysis/                     # Analysis features
│   ├── dashboard/                    # Dashboard widgets
│   ├── filters/                      # Filter controls
│   ├── journal/                      # Journal features
│   ├── layout/                       # Layout components
│   ├── portfolio/                    # Portfolio widgets
│   ├── ui/                           # Reusable UI
│   └── wallet/                       # Wallet integration
│
├── lib/                              # Core library
│   ├── mock-data.ts                  # Mock data
│   ├── types.ts                      # TypeScript types
│   ├── utils.ts                      # Utility functions
│   └── __tests__/                    # Unit tests
│
└── public/                           # Static assets
Directory Responsibilities
Directory	Responsibility	Naming Convention
app/	Page routing and layouts	page.tsx, layout.tsx
components/	UI components	PascalCase.tsx
lib/	Business logic	kebab-case.ts
public/	Static files	lowercase
3. Component Architecture
Component Hierarchy
RootLayout
├── ThemeProvider
│   └── ErrorBoundary
│       ├── Sidebar
│       │   ├── Navigation Links
│       │   ├── ThemeToggle
│       │   └── User Profile
│       │
│       ├── Main Content
│       │   └── [Page Component]
│       │       ├── Header
│       │       ├── Content Grid
│       │       │   ├── StatsGrid
│       │       │   ├── Charts
│       │       │   └── Tables
│       │       └── Footer
│       │
│       └── BottomNav (Mobile)
Component Categories
1. Layout Components
Located in components/layout/

Component	Purpose	Props
Sidebar	Desktop navigation	None
BottomNav	Mobile navigation	None
2. UI Components
Located in components/ui/

Component	Purpose	Key Features
ErrorBoundary	Error handling	Retry functionality
Loading	Loading states	Multiple variants
ThemeToggle	Theme switching	localStorage sync
3. Feature Components
Located in feature-specific directories

Directory	Components	Features
dashboard/	StatsGrid, EquityChart	Metrics display
journal/	JournalTable, AddTradeModal	Trade management
portfolio/	AssetAllocation, RiskMetrics	Portfolio analysis
analysis/	FeeBreakdown, TimeAnalysis	Advanced metrics
Component Design Patterns
Container/Presentation Pattern
// Container: Handles data and logic
function JournalTableContainer() {
  const [trades, setTrades] = useState([]);
  const filteredTrades = filterTrades(trades);
  
  return <JournalTablePresentation trades={filteredTrades} />;
}

// Presentation: Pure UI rendering
function JournalTablePresentation({ trades }) {
  return <table>...</table>;
}
Compound Components Pattern
<Modal>
  <Modal.Header>Title</Modal.Header>
  <Modal.Body>Content</Modal.Body>
  <Modal.Footer>Actions</Modal.Footer>
</Modal>
4. Data Layer
Data Flow Diagram
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  mock-data.ts │────▶│   utils.ts   │────▶│  Component   │
│              │      │              │      │              │
│ • trades     │      │ • calculate  │      │ • render     │
│ • assets     │      │ • filter     │      │ • display    │
│ • fees       │      │ • format     │      │              │
└──────────────┘      └──────────────┘      └──────────────┘
Type Definitions
// Core trade data structure
interface TradeData {
  id: string;
  pair: string;
  side: 'LONG' | 'SHORT';
  size: string;
  entry: number;
  exit: number;
  fee: number;
  pnl: number;
  date: string;
  entryTime: string;
  exitTime: string;
  duration: number;
  notes: string;
  tags: string[];
  volume: number;
}
Utility Functions Architecture
utils.ts
│
├── Formatting Layer
│   ├── formatCurrency()
│   ├── formatPercentage()
│   ├── formatDuration()
│   └── getProfitColor()
│
├── Calculation Layer
│   ├── calculateWinRate()
│   ├── calculateProfitFactor()
│   ├── calculateAverageDuration()
│   ├── calculateTotalVolume()
│   └── getBestAndWorstTrade()
│
└── Filter Layer
    ├── filterTradesBySymbol()
    ├── filterTradesByDateRange()
    └── getUniqueSymbols()
5. State Management
State Categories
Category	Solution	Scope	Persistence
Theme	React Context	Global	localStorage
UI State	useState	Component	Memory
Form State	useState	Component	Memory
URL State	Next.js Router	Page	URL
Theme Context Architecture
// Provider structure
ThemeContext
├── theme: 'dark' | 'light'
├── toggleTheme: () => void
└── mounted: boolean

// Usage
const { theme, toggleTheme } = useTheme();
Local State Patterns
// Component with multiple state concerns
function JournalTable() {
  // UI state
  const [searchTerm, setSearchTerm] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);
  
  // Filter state
  const [selectedSymbol, setSelectedSymbol] = useState('ALL');
  const [dateRange, setDateRange] = useState({ start, end });
  
  // Loading state
  const [isExporting, setIsExporting] = useState(false);
}
6. Styling Architecture
CSS Custom Properties
/* Theme variables in globals.css */
:root {
  /* Colors */
  --color-primary: #f2b90d;
  --color-profit: #10B981;
  --color-loss: #EF4444;
  
  /* Backgrounds */
  --bg-primary: #0F0F0F;
  --bg-surface: #1A1A1A;
  
  /* Typography */
  --font-display: "Space Grotesk";
  --font-body: "Inter";
  --font-mono: "Roboto Mono";
  
  /* Shadows */
  --shadow-neobrutal: 4px 4px 0px 0px rgba(0,0,0,1);
}
Design Tokens
Token	Dark	Light
--bg-primary	#0F0F0F	#F8F8F5
--bg-surface	#1A1A1A	#FFFFFF
--text-primary	#FFFFFF	#1F2937
--text-secondary	#9CA3AF	#6B7280
--border-color	#333333	#E5E7EB
Neobrutalist Design System
/* Standard card styling */
.card {
  @apply bg-surface-dark;
  @apply neobrutal-border;
  @apply p-4;
  @apply shadow-neobrutal;
}

/* Primary button */
.btn-primary {
  @apply bg-primary text-black;
  @apply border-2 border-black;
  @apply shadow-neobrutal-sm;
  @apply hover:translate-x-[1px] hover:translate-y-[1px];
  @apply hover:shadow-none;
}
7. Error Handling
Error Boundary Pattern
class ErrorBoundary extends Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback onRetry={this.handleRetry} />;
    }
    return this.props.children;
  }
}
Input Validation
// Sanitization constants
const MAX_SEARCH_LENGTH = 100;
const INVALID_CHARS_REGEX = /[<>{}[\]\\]/g;

// Validation function
function sanitizeSearchInput(input: string): string {
  return input
    .slice(0, MAX_SEARCH_LENGTH)
    .replace(INVALID_CHARS_REGEX, '')
    .trim();
}
8. Testing Strategy
Test Pyramid
         ┌───────────┐
         │    E2E    │  (Future)
         │   Tests   │
        ┌┴───────────┴┐
        │ Integration │  (Future)
        │    Tests    │
       ┌┴─────────────┴┐
       │  Unit Tests   │  ✅ Implemented
       │  (20+ tests)  │
       └───────────────┘
Unit Test Coverage
Function	Tests	Coverage
formatCurrency	3	100%
calculateWinRate	3	100%
calculateProfitFactor	3	100%
filterTradesBySymbol	3	100%
Test Patterns
describe('calculateWinRate', () => {
  it('calculates correctly for mixed trades', () => {
    expect(calculateWinRate(mockTrades)).toBeCloseTo(66.67, 1);
  });

  it('handles empty array', () => {
    expect(calculateWinRate([])).toBe(0);
  });

  it('handles all winners', () => {
    const winners = mockTrades.filter(t => t.pnl > 0);
    expect(calculateWinRate(winners)).toBe(100);
  });
});
9. Performance Considerations
Client-Side Optimizations
Technique	Implementation
Code Splitting	Next.js automatic
Lazy Loading	Dynamic imports
Memoization	useCallback, useMemo
Debouncing	Search input
Bundle Optimization
// next.config.ts
module.exports = {
  productionBrowserSourceMaps: false,
  compress: true,
  poweredByHeader: false,
};
Loading States
// Skeleton loading for tables
function TableRowSkeleton({ columns = 8 }) {
  return (
    <tr className="animate-pulse">
      {Array.from({ length: columns }).map((_, i) => (
        <td key={i}>
          <div className="h-4 bg-white/5 rounded" />
        </td>
      ))}
    </tr>
  );
}
10. Security Measures
Input Sanitization
Attack Vector	Protection
XSS	Regex character filtering
Injection	Input length limits
CSRF	Next.js built-in
Security Implementations
// XSS prevention
const INVALID_CHARS = /[<>{}[\]\\]/g;
input.replace(INVALID_CHARS, '');

// Length limiting
const MAX_LENGTH = 100;
input.slice(0, MAX_LENGTH);

// Safe defaults
if (context === undefined) {
  return { theme: 'dark', toggleTheme: () => {} };
}
Content Security Policy (Recommended)
// next.config.ts
headers: [
  {
    key: 'Content-Security-Policy',
    value: "default-src 'self'; script-src 'self' 'unsafe-inline'",
  },
];
Appendix
Development Workflow
1. Create feature branch
2. Implement changes
3. Add tests
4. Run lint: npm run lint
5. Run tests: npm test
6. Build: npm run build
7. Create PR
Code Standards
TypeScript strict mode
JSDoc for public functions
Functional components
Custom hooks for logic
---

# 🏗️ LiquidityHawk Architecture
System Overview
LiquidityHawk is a modular Python-based trading bot designed for real-time market analysis and signal generation. The architecture follows a layered approach with clear separation of concerns.

┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   CLI (main) │  │  Dashboard   │  │   Telegram Alerts    │  │
│  │   main.py    │  │ dashboard.py │  │ telegram_bot.py      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MONITORING LAYER                            │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   TradingMonitor                          │  │
│  │  - Alert conditions (Oversold, Overbought, Extreme L/S)  │  │
│  │  - Liquidity hunt detection                               │  │
│  │  - Callback system for notifications                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      STRATEGY LAYER                             │
│  ┌────────────────────┐  ┌────────────────────────────────┐    │
│  │  ArbitrageStrategy │  │       CopyTrader               │    │
│  │  - Polymarket      │  │  - Wallet monitoring           │    │
│  │  - YES/NO spreads  │  │  - Trade replication           │    │
│  └────────────────────┘  └────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATA LAYER                                │
│  ┌────────────────────┐  ┌────────────────────────────────┐    │
│  │  MarketCollector   │  │      ExchangeMonitor           │    │
│  │  - Polymarket API  │  │  - BinanceTracker              │    │
│  │  - Order books     │  │  - BybitTracker                │    │
│  │  - Arbitrage scan  │  │  - TechnicalIndicators         │    │
│  └────────────────────┘  └────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EXECUTION LAYER                              │
│  ┌────────────────────┐  ┌────────────────────────────────┐    │
│  │    OrderManager    │  │       RiskManager              │    │
│  │  - Limit orders    │  │  - Position sizing             │    │
│  │  - Market orders   │  │  - Daily loss limits           │    │
│  │  - Order tracking  │  │  - Emergency stop              │    │
│  └────────────────────┘  └────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL SERVICES                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────────────┐    │
│  │ Binance  │ │  Bybit   │ │Polymarket│ │ Polygon (Web3)  │    │
│  │ Futures  │ │   API    │ │   CLOB   │ │   Blockchain    │    │
│  └──────────┘ └──────────┘ └──────────┘ └─────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
Module Details
1. Configuration (src/config.py)
Central configuration management using dataclasses and environment variables.

@dataclass
class BotConfig:
    polymarket: PolymarketConfig
    wallet: WalletConfig
    risk: RiskConfig
    copy_trade: CopyTradeConfig
    mode: str = "paper"
Environment Variables:

Variable	Description	Required
POLYMARKET_API_KEY	Polymarket API key	For Polymarket features
POLYMARKET_API_SECRET	API secret	For Polymarket features
POLYGON_RPC_URL	Alchemy/Infura RPC	For wallet tracking
TELEGRAM_BOT_TOKEN	Telegram bot token	For alerts
TELEGRAM_CHAT_ID	Your Telegram chat ID	For alerts
MAX_POSITION_SIZE_USD	Max single position	Yes
DAILY_LOSS_LIMIT_USD	Daily loss limit	Yes
2. Data Layer
ExchangeTracker (src/data/exchange_tracker.py)
Fetches real-time data from exchanges.

class BinanceTracker:
    async def get_long_short_ratio(symbol, period) -> LongShortRatio
    async def get_top_trader_ratio(symbol, period) -> LongShortRatio
    async def get_funding_rate(symbol) -> FundingRate
    async def get_klines(symbol, interval, limit) -> list[OHLCV]

class TechnicalIndicators:
    @staticmethod
    def williams_r(candles, period=14) -> WilliamsR
    @staticmethod
    def rsi(candles, period=14) -> float
Data Structures:

@dataclass
class LongShortRatio:
    symbol: str
    long_ratio: float   # Percentage (0-100)
    short_ratio: float  # Percentage (0-100)
    timestamp: datetime

@dataclass
class WilliamsR:
    value: float        # -100 to 0
    is_overbought: bool # value > -20
    is_oversold: bool   # value < -80
MarketCollector (src/data/market_collector.py)
Polymarket-specific data collection.

class MarketDataCollector:
    async def get_markets(active_only=True) -> list[Market]
    async def get_order_book(token_id) -> OrderBook
    async def find_arbitrage_opportunities(min_profit=1.0) -> list[dict]
3. Monitoring Layer
TradingMonitor (src/monitoring/trading_monitor.py)
Central monitoring with alert conditions.

class TradingMonitor:
    conditions: list[AlertCondition]
    
    async def start(symbols, interval, print_updates)
    async def check_and_alert(analysis)
Alert Conditions:

Condition	Trigger
OversoldCondition	Williams %R < -80
OverboughtCondition	Williams %R > -20
ExtremeLongShortCondition	L/S > 65%
ExtremeFundingCondition	Funding > 0.05%
LiquidityHuntCondition	Combined signals
TelegramAlertBot (src/monitoring/telegram_bot.py)
Telegram notification system.

class TelegramAlertBot:
    async def send_message(text, parse_mode="Markdown")
    async def send_signal(symbol, direction, entry_price, reason)
    async def send_long_short_update(symbol, long_ratio, short_ratio, williams_r)
    async def send_liquidity_alert(symbol, level, liquidation_amount)
4. Strategy Layer
ArbitrageStrategy (src/strategy/arbitrage.py)
Polymarket arbitrage detection and execution.

class ArbitrageStrategy:
    async def scan_opportunities(min_profit_percent) -> list[ArbitrageOpportunity]
    async def execute_arbitrage(opportunity, investment_usd, dry_run)
    async def run_continuous(investment, min_profit, interval, dry_run)
Arbitrage Logic:

If YES_ask + NO_ask < $1.00:
    profit = $1.00 - (YES_ask + NO_ask)
    Buy both YES and NO tokens
    Guaranteed profit when market resolves
CopyTrader (src/strategy/copy_trader.py)
Wallet copy trading.

class CopyTrader:
    async def start(target_wallet, live_mode)
    async def copy_trade(trade, dry_run) -> CopyTradeResult
    
    # Filters
    def set_filters(min_size, max_size, allowed_tokens)
5. Execution Layer
OrderManager (src/execution/order_manager.py)
Order placement and management.

class OrderManager:
    async def create_limit_order(token_id, side, price, size, order_type)
    async def create_market_order(token_id, side, size)
    async def cancel_order(order_id)
    async def get_open_orders()
Order Types:

GTC - Good Till Cancelled
FOK - Fill Or Kill
GTD - Good Till Date
RiskManager (src/risk/risk_manager.py)
Risk controls and safety limits.

class RiskManager:
    def check_trade_allowed(size, price, side) -> (bool, reason)
    def record_trade(token_id, side, price, size, pnl)
    def emergency_stop(reason)
    def get_stats() -> dict
Risk Features:

Daily P&L tracking
Maximum position size
Automatic stop on loss limit
Trade count limits
6. User Interfaces
CLI (main.py)
Click-based command-line interface.

# Commands
python main.py analyze --symbol BTCUSDT
python main.py longshort --symbol ETHUSDT --period 5m
python main.py monitor --symbols BTCUSDT,ETHUSDT --interval 60
python main.py scan --min-profit 0.5
python main.py arbitrage --investment 10 --mode paper
python main.py copy --wallet 0x... --scale 0.1
python main.py track --wallet 0x... --limit 20
python main.py status
Web Dashboard (dashboard.py)
FastAPI-based web interface.

# Endpoints
GET /                        # Dashboard HTML
GET /api/analysis/{symbol}   # JSON analysis data
Features:

Real-time price display
Visual L/S ratio bar
Indicator cards (W%R, RSI, Funding)
Auto-refresh (30 seconds)
Trading signal detection
Data Flow
Signal Detection Flow
1. ExchangeMonitor.get_full_analysis(symbol)
   ├── BinanceTracker.get_long_short_ratio()
   ├── BinanceTracker.get_top_trader_ratio()
   ├── BinanceTracker.get_funding_rate()
   ├── BinanceTracker.get_klines()
   └── TechnicalIndicators.williams_r()

2. TradingMonitor.check_and_alert(analysis)
   ├── OversoldCondition.check()
   ├── OverboughtCondition.check()
   ├── ExtremeLongShortCondition.check()
   └── LiquidityHuntCondition.check()

3. If condition triggered:
   ├── Print to console
   └── TelegramAlertBot.send_message()
Arbitrage Flow
1. MarketDataCollector.get_markets()

2. For each market:
   ├── get_order_book(YES_token)
   ├── get_order_book(NO_token)
   └── Calculate: YES_ask + NO_ask < $1.00?

3. If profitable:
   ├── RiskManager.check_trade_allowed()
   ├── OrderManager.create_limit_order(YES)
   └── OrderManager.create_limit_order(NO)

4. Track and report
Technology Stack
Component	Technology
Language	Python 3.10+
Web Framework	FastAPI + Uvicorn
HTTP Client	httpx (async)
Blockchain	web3.py
CLI	Click + Rich
Config	python-dotenv
API Rate Limits
Service	Limit	Notes
Binance	1200/min	Public endpoints
Bybit	120/min	Per endpoint
Polymarket	100/min	Authenticated
Polygonscan	5/sec	Free tier
Telegram	30/sec	Per chat
Security Considerations
Never commit .env - Contains secrets
Use paper mode first - Test thoroughly
Set loss limits - Protect capital
Secure VPS - Use SSH keys, firewall
Monitor logs - Watch for errors
Future Enhancements
 WebSocket connections for real-time data
 Multiple exchange support (OKX, Kraken)
 Machine learning signal enhancement
 Portfolio tracking and analytics
 Mobile app integration
 Backtesting framework
Architecture Version: 1.0.0
