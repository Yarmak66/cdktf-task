# Default environment
ENV ?= dev
ENV_FILE := .env.$(ENV)

# Check if the .env file exists
ifeq (,$(wildcard $(ENV_FILE)))
$(error ❌ Env file '$(ENV_FILE)' not found)
endif

# Export environment variables from the env file
include $(ENV_FILE)
export

.PHONY: get synth diff deploy destroy clean redeploy

get:
	cdktf get

synth:
	ENV=$(ENV) set -a && . $(ENV_FILE) && set +a && cdktf synth

diff:
	ENV=$(ENV) set -a && . $(ENV_FILE) && set +a && cdktf diff

deploy:
	ENV=$(ENV) set -a && . $(ENV_FILE) && set +a && cdktf deploy --auto-approve

destroy:
	ENV=$(ENV) set -a && . $(ENV_FILE) && set +a && cdktf destroy --auto-approve

clean:
	rm -rf .terraform .terraform.lock.hcl cdktf.out terraform.tfstate terraform.tfstate.backup

redeploy: clean get synth deploy
