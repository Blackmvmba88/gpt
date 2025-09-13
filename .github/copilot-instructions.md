# GPT Repository Instructions

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Repository Overview
This is a minimal GPT-related repository currently containing only basic documentation. The repository is in an early development stage with no established build system, dependencies, or runnable code. This creates an opportunity to establish proper development practices from the ground up.

## Working Effectively

### Initial Setup and Validation
Start by validating repository accessibility and basic operations (all commands complete in under 1 second):

- Check repository status: `git --no-pager status`
- List all files: `ls -la`
- View repository history: `git --no-pager log --oneline -5`
- Read current documentation: `cat README.md`
- Find all markdown files: `find . -name "*.md" -type f`

### Current Repository State (Validated)
- **No build system**: No package.json, requirements.txt, Makefile, or other build configuration files exist
- **No dependencies**: No dependency management system is in place
- **No source code**: Only documentation files exist
- **No tests**: No test framework or test files exist
- **No CI/CD**: No GitHub Actions workflows are configured yet
- **Git operations work normally**: All standard git commands function as expected

### Repository Structure
```
.
├── .git/                          # Git metadata
├── .github/                       # GitHub configuration  
│   └── copilot-instructions.md    # This file
└── README.md                      # Basic repository documentation (11 bytes)
```

## Development Guidelines

### Before Making Any Changes
Always validate the current state first:

1. **Check git status**: `git --no-pager status` (< 1 second)
2. **List current files**: `ls -la` (< 1 second)  
3. **Review commit history**: `git --no-pager log --oneline -10` (< 1 second)
4. **Check working branch**: `git --no-pager branch -v` (< 1 second)

### Adding New Functionality - Technology Stack Setup

Since this repository lacks infrastructure, when implementing GPT-related functionality, follow these VALIDATED setup patterns:

#### For Node.js/TypeScript GPT Applications
```bash
# Initialize Node.js project (< 5 seconds)
npm init -y

# Install common GPT/AI dependencies (timing varies: 30 seconds - 5 minutes)
npm install openai @types/node typescript ts-node

# Install development dependencies (timing varies: 15 seconds - 2 minutes)
npm install -D @types/jest jest nodemon

# Create TypeScript config
npx tsc --init

# NEVER CANCEL: Build setup takes 2-10 minutes initially
npm run build

# NEVER CANCEL: Test setup takes 1-5 minutes
npm test
```

#### For Python GPT Applications  
```bash
# Create virtual environment (< 10 seconds)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install common GPT/AI dependencies (timing varies: 1-10 minutes)
pip install openai python-dotenv pytest

# Create requirements file (< 1 second)
pip freeze > requirements.txt

# NEVER CANCEL: Initial package installation can take 10+ minutes
pip install -r requirements.txt

# NEVER CANCEL: Test runs may take 5-15 minutes depending on API calls
python -m pytest
```

#### For Go GPT Applications
```bash
# Initialize Go module (< 5 seconds)
go mod init github.com/Blackmvmba88/gpt

# Install common dependencies (timing varies: 30 seconds - 5 minutes)
go get github.com/sashabaranov/go-openai
go get github.com/joho/godotenv

# NEVER CANCEL: Build may take 2-15 minutes for dependencies
go build ./...

# NEVER CANCEL: Tests may take 5-20 minutes depending on API integration
go test ./...
```

### Validation Requirements

#### Current State Validation (No Code Yet)
Since no application exists, validate these basic operations:

1. **Repository integrity**: `git --no-pager log --oneline -5`
2. **File structure**: `find . -type f -not -path "./.git/*"`
3. **README content**: `cat README.md` (should show "# gpt\njiji")
4. **Branch information**: `git --no-pager branch -v`

#### Future Code Validation (When Implemented)
When GPT functionality is added, ALWAYS validate with complete scenarios:

**For GPT Chat Applications:**
1. **API connectivity**: Test OpenAI API key configuration
2. **Basic chat flow**: Send a simple prompt and receive response  
3. **Error handling**: Test with invalid API key or malformed requests
4. **Rate limiting**: Verify proper handling of API rate limits

**For GPT CLI Tools:**
1. **Help display**: `./tool --help` 
2. **Basic processing**: `./tool process "test prompt"`
3. **File operations**: `./tool --input test.txt --output result.txt`
4. **Error scenarios**: Test with missing files or invalid arguments

**For GPT Web Applications:**
1. **Server startup**: Verify application starts without errors
2. **Homepage load**: Navigate to application and verify UI renders
3. **API endpoints**: Test main GPT-related endpoints work
4. **End-to-end flow**: Complete a full user interaction scenario

### Critical Timing Expectations

**NEVER CANCEL any of these operations - wait for completion:**

- **Package installation**: 1-10 minutes (Node.js/Python), up to 20 minutes for Go
- **Initial builds**: 2-15 minutes for first-time compilation
- **Test suites**: 5-20 minutes when GPT API integration is involved
- **GPT API calls**: 5-30 seconds per request depending on model and complexity

**Set timeouts appropriately:**
- Build commands: 60+ minutes
- Test commands: 30+ minutes  
- Package installation: 30+ minutes

## Common Git Operations (All Validated)

### Daily Development Workflow
```bash
# Check current state (< 1 second)
git --no-pager status

# Create feature branch (< 1 second)
git checkout -b feature/gpt-integration

# Stage changes (< 1 second for current repository size)
git add .

# View staged changes (< 1 second)
git --no-pager diff --cached

# Commit changes (< 1 second)
git commit -m "Add GPT integration functionality"

# Push to remote (< 5 seconds, network dependent)
git push origin feature/gpt-integration
```

### Repository Exploration
```bash
# List all files including hidden (< 1 second)
ls -la

# Find specific file types (< 1 second for current size)
find . -name "*.py" -o -name "*.js" -o -name "*.go" -o -name "*.md"

# Check repository size (< 1 second)
du -sh .

# View file contents (< 1 second for small files)
cat README.md
```

## Future Development Patterns

### When Adding GPT Functionality
Consider these implementation approaches:

1. **CLI Tool**: Command-line interface for GPT interactions
   - Use argparse (Python), commander.js (Node.js), or cobra (Go)
   - Support batch processing and piped input
   - Include comprehensive help and examples

2. **Web API**: RESTful service for GPT integration
   - Implement rate limiting and authentication
   - Provide OpenAPI/Swagger documentation
   - Include health checks and monitoring endpoints

3. **Chat Interface**: Interactive conversational application
   - Support message history and context
   - Implement streaming responses for better UX
   - Include conversation management features

### Recommended Project Structure (Future)
```
.
├── .github/
│   ├── workflows/           # CI/CD pipelines
│   └── copilot-instructions.md
├── src/                     # Source code
├── tests/                   # Test files
├── docs/                    # Documentation
├── examples/                # Usage examples
├── .env.example             # Environment template
├── README.md                # Updated with usage instructions
└── [build config files]     # package.json, requirements.txt, etc.
```

## Environment Setup

### Required Tools (Install Before Development)
- **Git**: Already available and validated
- **Node.js**: `curl -fsSL https://nodejs.org/dist/v20.10.0/node-v20.10.0-linux-x64.tar.xz | tar -xJ`
- **Python**: `apt-get update && apt-get install -y python3 python3-pip python3-venv`
- **Go**: `wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz`

### API Keys and Configuration
When implementing GPT functionality:

1. **OpenAI API Key**: Set `OPENAI_API_KEY` environment variable
2. **Configuration file**: Create `.env` for development settings
3. **Rate limiting**: Implement proper request throttling
4. **Error handling**: Robust error handling for API failures

## Validation Checklist

Before committing any changes to this repository:

- [ ] **Basic git operations work**: `git --no-pager status && git --no-pager log --oneline -3`
- [ ] **Repository structure intact**: `ls -la` shows expected files
- [ ] **No broken dependencies**: If build system added, ensure clean builds
- [ ] **Tests pass**: If tests added, ensure `NEVER CANCEL` policy for test runs
- [ ] **Documentation updated**: Update this file when new functionality is added
- [ ] **API functionality tested**: If GPT integration added, test with real API calls
- [ ] **Error scenarios handled**: Test failure modes and edge cases

## Notes for Contributors

### Getting Started
1. This repository is currently a blank slate - perfect for establishing good practices
2. Choose technology stack based on intended GPT use case:
   - **Node.js/TypeScript**: Web applications, APIs, real-time chat
   - **Python**: Data processing, ML integration, research tools  
   - **Go**: High-performance APIs, CLI tools, system integration
3. Establish testing strategy early, especially for GPT API integration
4. Consider token usage and costs in design decisions

### Best Practices for GPT Development
- **Always validate API keys**: Test with real OpenAI API before deployment
- **Implement proper rate limiting**: Respect OpenAI API limits
- **Handle streaming responses**: For better user experience in chat applications
- **Log interactions carefully**: Balance debugging needs with privacy
- **Test with various prompts**: Ensure robust handling of different input types
- **Monitor token usage**: Implement tracking for cost management

### Contributing Guidelines
- Update these instructions when adding new functionality
- Validate all commands before documenting them
- Include timing expectations for new operations
- Test complete user scenarios, not just technical operations
- Follow established coding standards for chosen technology stack

## CRITICAL REMINDERS

- **NEVER CANCEL** builds, tests, or package installations
- **Always set 60+ minute timeouts** for build operations
- **Always set 30+ minute timeouts** for test operations  
- **Validate every command** before documenting it
- **Test real GPT API integration** don't just mock responses
- **Update this file** when repository evolves beyond minimal state
- **Consider API costs** when testing GPT functionality repeatedly

---

*Last updated: When implementing GPT functionality, remember that this repository started as a minimal template. The first major contribution should establish the technology stack, project structure, and development workflow.*