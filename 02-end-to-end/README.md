# LiveCodeInterview

Real-time collaborative coding interview platform for technical assessments.

## Overview

LiveCodeInterview enables real-time collaborative coding sessions with:
- Instant code synchronization across all participants
- Python and JavaScript execution in browser via WebAssembly
- NumPy and Pandas support for data science interviews
- Syntax highlighting with Monaco Editor (VS Code's editor)
- Shared output console with real-time updates
- Presence tracking to see active participants
- Dark/Light theme support

## Technology Stack

### Frontend
- React 18 with Vite
- Monaco Editor for code editing
- Socket.IO client for real-time synchronization
- Modern CSS with glassmorphism effects

### Backend
- Node.js with Express
- Socket.IO server for WebSocket connections
- In-memory session storage
- Rate limiting and security headers

### Code Execution
- **JavaScript**: Browser Web Workers (sandboxed execution)
- **Python**: Pyodide (Python compiled to WebAssembly)
- **Libraries**: NumPy, Pandas (auto-installed on first use)

## Live demo
https://livecodeinterview.onrender.com/

> Note: the first load may take up to 30–50 seconds on Render Free tier.

## Quick Start

### Prerequisites

- Node.js 18 or higher
- npm package manager

### Installation

```bash
# Install all dependencies
make install

# Or manually:
npm install
cd client && npm install && cd ..
cd server && npm install && cd ..
```

### Running the Application

**Development Mode (Recommended):**

```bash
# Run both client and server concurrently
make dev

# Or manually:
npm run dev
```

This starts:
- Backend server on `http://localhost:3001`
- Frontend client on `http://localhost:5173`

**Run Separately:**

```bash
# Terminal 1 - Backend
make dev-server

# Terminal 2 - Frontend
make dev-client
```

### Usage

1. Open browser to `http://localhost:5173`
2. Click "Create Interview Session"
3. Share the session URL with candidates
4. Start coding together in real-time

## Development

### Available Commands

Run `make help` to see all available commands:

```bash
make install        # Install all dependencies
make dev            # Run development server
make test           # Run all tests
make build          # Build production client
make docker-build   # Build Docker image
make clean          # Remove node_modules and build artifacts
```

### Git Commit Hooks

Install commit message validation:

```bash
make setup-commit-hook
```

This enforces conventional commit prefixes:
- `feat:` - New features
- `fix:` - Bug fixes
- `refactor:` - Code refactoring
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks
- `style:` - Code formatting
- `perf:` - Performance improvements

## Testing

The project includes comprehensive test coverage:

### Run All Tests

```bash
make test
```

### Server Tests (26 tests)

```bash
make test-server
```

**Coverage:**
- Session store unit tests (15 tests)
- REST API integration tests (5 tests)
- Socket.IO integration tests (6 tests)

### Client Tests (46 tests)

```bash
make test-client
```

**Coverage:**
- Hook tests (useTheme, useCodeExecution)
- Component tests (ThemeToggle, CodeEditor, LanguageSelector)
- Integration tests

### Watch Mode

```bash
cd server && npm run test:watch
# or
cd client && npm run test:watch
```

## Deployment

### Docker

Build and run the application in a container:

```bash
# Build Docker image
make docker-build

# Run container (exposed on port 3000)
make docker-run

# Or manually:
docker build -t livecodeinterview:latest .
docker run -p 3000:3000 livecodeinterview:latest
```

The Docker image:
- Uses multi-stage build for optimization
- Runs as non-root user for security
- Includes only production dependencies
- Serves built frontend from backend

## Project Structure

```
.
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── pages/          # Page components
│   │   └── workers/        # Web Workers for code execution
│   ├── tests/              # Client-side tests
│   └── package.json
│
├── server/                 # Express backend
│   ├── src/
│   │   ├── routes/         # REST API endpoints
│   │   ├── socket/         # Socket.IO event handlers
│   │   └── store/          # In-memory session storage
│   ├── tests/              # Server-side tests
│   └── package.json
│
├── Dockerfile              # Multi-stage Docker build
├── Makefile                # Development commands
├── LICENSE                 # MIT License
└── package.json            # Root package configuration
```

## API Documentation

### REST Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/sessions` | Create a new coding session |
| GET | `/api/sessions/:id` | Get session details |
| GET | `/health` | Health check endpoint |

### Socket.IO Events

| Event | Direction | Description |
|-------|-----------|-------------|
| `join-session` | Client → Server | Join a session room |
| `session-state` | Server → Client | Receive initial session state |
| `code-change` | Client → Server | Send code update |
| `code-update` | Server → Client | Receive code update from others |
| `language-change` | Client → Server | Change programming language |
| `language-update` | Server → Client | Receive language update |
| `output-change` | Client → Server | Send execution output |
| `output-update` | Server → Client | Receive execution output |
| `activity-change` | Client → Server | Update user activity status |
| `presence-update` | Server → Client | Receive presence information |

## Features

### Real-time Collaboration
- Instant code synchronization across all participants
- Live presence indicators
- Session-based isolation

### Code Execution
- Client-side execution (no server-side code running)
- JavaScript execution in Web Workers
- Python execution via Pyodide (WebAssembly)
- Automatic NumPy and Pandas installation
- Shared output console
- Error handling and timeout protection

### User Interface
- Monaco Editor (VS Code's editor)
- Syntax highlighting for multiple languages
- Dark and light theme support
- Responsive design for mobile and desktop
- Glassmorphism effects
- Purple/violet color scheme

### Security
- Client-side code execution only
- Sandboxed JavaScript execution
- Rate limiting on API endpoints
- Content Security Policy headers
- Helmet.js security middleware
- Non-root Docker container

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built with modern web technologies and best practices for real-time collaborative applications.
