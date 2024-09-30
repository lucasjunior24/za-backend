deploy-local:
		docker build -t za_local:1.0 .
		docker-compose -f compose/compose-local/docker-compose.yml up -d
		
deploy-develop:
		docker build -t za_develop .
		docker-compose -f compose/compose-develop/docker-compose.yml up -d