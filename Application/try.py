from Application.models import player_stats
team_name='Sri Lanka'
player = player_stats.query.filter_by(country=team_name).all()
print(player)