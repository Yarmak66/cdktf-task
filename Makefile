# Default environment
ENV ?= dev
ENV_FILE := .env.$(ENV)

# Check if the .env file exists
ifeq (,$(wildcard $(ENV_FILE)))
$(error ❌ Env file '$(ENV_FILE)' not found)
endif

# Load environment variables from file
include $(ENV_FILE)
export

.PHONY: get synth diff deploy destroy clean redeploy

# Generate Terraform provider bindings
get:
	cdktf get

# Synthesize Terraform configuration from CDKTF
synth:
	set -a && source $(ENV_FILE) && set +a && cdktf synth

# Show planned infrastructure changes
diff:
	set -a && source $(ENV_FILE) && set +a && cdktf diff

# Apply infrastructure changes without confirmation
deploy:
	set -a && source $(ENV_FILE) && set +a && cdktf deploy --auto-approve

# Destroy all managed infrastructure
destroy:
	set -a && source $(ENV_FILE) && set +a && cdktf destroy --auto-approve

# Remove local state and cached files
clean:
	rm -rf .terraform .terraform.lock.hcl cdktf.out terraform.tfstate terraform.tfstate.backup

# Full teardown and redeploy
redeploy: clean get synth deploy
  