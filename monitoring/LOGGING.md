# Logging

Created docker-compose with **monitoring_logging** then added created services :
- simple_app
- loki
- promtail
- grafana
- prometheus

At the end run the docker-compose and setup data sources

## Best practices

- Defined network in docker-compose which I mentioned above
- Defined container names and image names
- Set mem limits
