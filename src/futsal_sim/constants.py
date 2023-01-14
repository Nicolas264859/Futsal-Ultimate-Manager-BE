# Player amount in team sheet
PLAYER_AMOUNT_TEAM_SHEET = 5

# Used when calculating team skill
TEAM_SKILL_CALC_PLAYER_AMOUNT = 8

# Formula for calculation: BASE_PRICE - team_avg + self.skill
BASE_PRICE_FOR_AVERAGE_PLAYER = 20

MIN_PLAYER_SELL_PRICE = 5

MAX_SQUAD_VALID_SIZE = 25

MIN_GOAL_AMOUNT = 0

MAX_GOAL_AMOUNT = 12

MIN_CPU_DIFFICULTY_RATING = 0

MAX_CPU_DIFFICULTY_RATING = 10

GOAL_AMOUNT_GENERATION_ITERATIONS = 3

MULTIPLIER_COIN_DRAW = 0.4

MULTIPLIER_COIN_LOSS = 0.125

# ---------------------------------------------------
# Percentage chances for positions doing an action during a match

# Scoring a goal. Percentages must add up 100!
ATTACKER_GOAL_PERC = 72
DEFENDER_GOAL_PERC = 26
GK_GOAL_PERC = 2

# Assisting a goal. Percentages must add up 100!
ATTACKER_ASSIST_PERC = 56
DEFENDER_ASSIST_PERC = 40
GK_ASSIST_PERC = 4

# ----------------------------------------------------
# Multipliers for player skills

# Player favourite position equals playing position
MULTIPLIER_PLAYER_FAV_POS = 1

# Gk playing in a different position
MULTIPLIER_GK_INFIELD = 0.5

# Infield player(attacker defender) playing in a different position
MULTIPLIER_DIFFERENT_INFIELD_POS = 0.75

MULTIPLIER_INFIELD_AS_GK = 0.25

STAMINA_EFFECT = True


# -----------------------------------------------
# Packs
PLAYER_AMOUNT_IN_PACK = 3
BRONZE_PRICE = 100
SILVER_PRICE = 200
GOLD_PRICE = 400

# Coin generation upper, lower bounds (is added to avg_skill of team)
GOLD_LOWER_BOUND = 0
GOLD_UPPER_BOUND = 8

SILVER_LOWER_BOUND = -3
SILVER_UPPER_BOUND = 3

BRONZE_LOWER_BOUND = -10
BRONZE_UPPER_BOUND = 0

# Player generation used in packs, and during team creation
GK_GENERATION_PERC_CHANCE = 20
DEF_GENERATION_PERC_CHANCE = 40
ATT_GENERATION_PERC_CHANCE = 40

# ---------------------------------------------
# Team Creation
BASE_COIN_AMOUNT = 100

# Created team will have players with skill in this interval
PLAYER_AMOUNT_CREATED_TEAM = 7

SKILL_LOWER_BOUND_CREATED_TEAM = 15
SKILL_UPPER_BOUND_CREATED_TEAM = 25
