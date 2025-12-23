.PHONY: help install dev test build docker-build docker-run clean setup-commit-hook test-commit-hook lint

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies (root, client, server)
	npm install
	cd client && npm install
	cd server && npm install

dev: ## Run development server (client + server concurrently)
	npm run dev

dev-server: ## Run only backend server
	cd server && npm run dev

dev-client: ## Run only frontend client
	cd client && npm run dev

test: ## Run all tests (client + server)
	npm test

test-server: ## Run server tests only
	cd server && npm test

test-client: ## Run client tests only
	cd client && npm test

test-watch: ## Run tests in watch mode
	cd server && npm run test:watch

build: ## Build production client
	cd client && npm run build

docker-build: ## Build Docker image
	docker build -t livecodeinterview:latest .

docker-run: ## Run Docker container
	docker run -p 3000:3000 livecodeinterview:latest

clean: ## Remove node_modules and build artifacts
	rm -rf node_modules client/node_modules server/node_modules
	rm -rf client/dist

format: ## Format code (if using prettier)
	cd client && npx prettier --write "src/**/*.{js,jsx}"
	cd server && npx prettier --write "src/**/*.js"

setup-commit-hook: ## Install Git commit-msg hook that enforces allowed prefixes
	@echo '#!/bin/sh' > .git/hooks/commit-msg
	@echo 'commit_msg=$$(head -1 "$$1")' >> .git/hooks/commit-msg
	@echo 'if ! echo "$$commit_msg" | grep -qiE "^(feat|fix|refactor|docs|test|chore|style|perf|revert|wip):"; then' >> .git/hooks/commit-msg
	@echo '  echo "ERROR: Commit message must start with one of: feat:, fix:, refactor:, docs:, test:, chore:, style:, perf:, revert:, wip:" >&2' >> .git/hooks/commit-msg
	@echo '  exit 1' >> .git/hooks/commit-msg
	@echo 'fi' >> .git/hooks/commit-msg
	@chmod +x .git/hooks/commit-msg
	@echo "✓ Commit hook installed successfully."

test-commit-hook: ## Test commit hook with invalid message (should fail)
	@echo "Testing commit hook with invalid message..."
	@echo 'test' > test-commit.txt
	@git add test-commit.txt
	@git commit -m 'invalid commit' || echo "✓ Commit rejected as expected."
	@rm -f test-commit.txt

lint: ## Run code linting (placeholder for future linting setup)
	@echo "Linting not configured yet. Add ESLint/Prettier setup."
