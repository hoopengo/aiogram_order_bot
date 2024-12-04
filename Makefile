restart:
	docker compose up -d --build && docker logs aiogram_order_bot-bot-1 --follow
stop:
	docker compose down -v
alembic-revision: # make alembic-revision COMMENT="your comment"
	docker exec -it aiogram_order_bot-bot-1 bash -c "alembic revision --autogenerate -m ${COMMENT}"
relogs:
	docker logs aiogram_order_bot-bot-1 --follow
psql:
	docker exec -it --user postgres aiogram_order_bot-db-1 psql
