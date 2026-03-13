#!/usr/bin/env bash
#
# setup.sh -- Install OMEGA Memory, an MCP memory server for persistent agent memory.
#
# Usage:
#   ./integrations/omega-memory/setup.sh

set -euo pipefail

echo "OMEGA Memory Integration Setup"
echo "==============================="
echo ""

# Check for Python 3.11+
PYTHON_CMD=""

for cmd in python3.11 python3.12 python3.13 python3; do
  if command -v "$cmd" &>/dev/null; then
    version=$("$cmd" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    major=$(echo "$version" | cut -d. -f1)
    minor=$(echo "$version" | cut -d. -f2)
    if [ "$major" -ge 3 ] && [ "$minor" -ge 11 ]; then
      PYTHON_CMD="$cmd"
      break
    fi
  fi
done

if [ -z "$PYTHON_CMD" ]; then
  echo "Error: Python 3.11+ is required but not found."
  echo ""
  echo "Install Python 3.11+ from https://www.python.org/downloads/"
  echo "or via your package manager:"
  echo "  brew install python@3.11      # macOS"
  echo "  sudo apt install python3.11   # Ubuntu/Debian"
  exit 1
fi

echo "Found $PYTHON_CMD ($($PYTHON_CMD --version))"
echo ""

# Install omega-memory
echo "Installing omega-memory..."
$PYTHON_CMD -m pip install omega-memory
echo ""
echo "omega-memory installed."
echo ""

# Check for existing MCP client configs
CONFIG_FOUND=false
CLAUDE_CONFIG="$HOME/.claude.json"

if [ -f "$CLAUDE_CONFIG" ]; then
  echo "Found Claude Code config at $CLAUDE_CONFIG"
  CONFIG_FOUND=true

  # Check if omega is already configured
  if grep -q '"omega"' "$CLAUDE_CONFIG" 2>/dev/null; then
    echo "OMEGA is already configured in Claude Code."
  else
    echo ""
    echo "Add OMEGA to your Claude Code config by adding this to the"
    echo "\"mcpServers\" section in $CLAUDE_CONFIG:"
    echo ""
    echo '    "omega": {'
    echo "      \"command\": \"$PYTHON_CMD\","
    echo '      "args": ["-m", "omega.server.mcp_server"]'
    echo '    }'
  fi
fi

if [ -f "$HOME/.cursor/mcp.json" ]; then
  echo "Found Cursor config at ~/.cursor/mcp.json"
  CONFIG_FOUND=true
fi

if [ -f ".mcp.json" ]; then
  echo "Found MCP config at .mcp.json"
  CONFIG_FOUND=true
fi

if [ "$CONFIG_FOUND" = false ]; then
  echo "No MCP client config found."
  echo ""
  echo "Add OMEGA to your MCP client config:"
  echo ""
  echo '  {'
  echo '    "mcpServers": {'
  echo '      "omega": {'
  echo "        \"command\": \"$PYTHON_CMD\","
  echo '        "args": ["-m", "omega.server.mcp_server"]'
  echo '      }'
  echo '    }'
  echo '  }'
fi

echo ""
echo "Setup complete."
echo ""
echo "Next steps:"
echo "  1. Add OMEGA to your MCP client config (see above)"
echo "  2. Start a new session — OMEGA tools will be available automatically"
echo "  3. Add a Memory Integration section to any agent prompt"
echo "     (see integrations/omega-memory/memory-section-template.md)"
