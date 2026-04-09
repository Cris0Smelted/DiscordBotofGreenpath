"""Challenge data for the Discord bot.

Provide a dictionary named `CHALLENGES` containing ecological and
environmental challenge items. Each item is a dict with keys:
- title: short title
- question: the prompt/question text
- options: list of choices (for multiple-choice)
- answer: canonical answer string
- points: integer points awarded for a correct answer
- tags: list of topical tags
- difficulty: one of 'easy', 'medium', 'hard'

This file is intentionally simple so the bot can import `CHALLENGES`
and use it to pick or display challenges.
"""

CHALLENGES = {
	"recycle_1": {
		"title": "Plastic Identification",
		"question": "Which plastic resin code is most commonly recycled into new beverage bottles?",
		"options": ["PET (1)", "HDPE (2)", "PVC (3)", "PS (6)"],
		"answer": "PET (1)",
		"tags": ["waste", "recycling", "materials"],
		"difficulty": "easy",
		"points": 1,
	},

	"water_1": {
		"title": "Water Conservation",
		"question": "Which of these actions saves the most household water over time?",
		"options": ["Taking shorter showers", "Fixing leaky taps", "Running dishwasher with full loads", "Turning off the tap while brushing"],
		"answer": "Fixing leaky taps",
		"tags": ["water", "conservation"],
		"difficulty": "easy",
		"points": 1,
	},

	"energy_1": {
		"title": "Renewable Energy",
		"question": "Which renewable energy source generates electricity without burning fuel and with near-zero direct CO2 emissions?",
		"options": ["Coal", "Natural gas", "Solar photovoltaics", "Diesel"],
		"answer": "Solar photovoltaics",
		"tags": ["energy", "climate"],
		"difficulty": "easy",
		"points": 1,
	},

	"biodiv_1": {
		"title": "Pollinators",
		"question": "Name one key reason why pollinators (like bees) are important for ecosystems and human food production.",
		"options": ["They pollinate crops", "They increase greenhouse gases", "They reduce soil fertility", "They create more waste"],
		"answer": "They pollinate crops",
		"tags": ["biodiversity", "ecosystems", "pollinators"],
		"difficulty": "easy",
		"points": 1,
	},

	"waste_1": {
		"title": "Composting Basics",
		"question": "Which of the following is NOT recommended for a home compost pile?",
		"options": ["Fruit and vegetable scraps", "Coffee grounds", "Meat and dairy", "Leaves and yard waste"],
		"answer": "Meat and dairy",
		"tags": ["waste", "composting"],
		"difficulty": "medium",
		"points": 1,
	},

	"climate_1": {
		"title": "Greenhouse Gases",
		"question": "Which gas is the largest contributor to human-caused global warming by volume?",
		"options": ["Carbon dioxide (CO2)", "Methane (CH4)", "Nitrous oxide (N2O)", "Ozone (O3)"],
		"answer": "Carbon dioxide (CO2)",
		"tags": ["climate", "ghg"],
		"difficulty": "easy",
		"points": 1,
	},

	"transport_1": {
		"title": "Sustainable Transport",
		"question": "Which transportation change typically reduces an individual's carbon footprint the most?",
		"options": ["Switch from car to public transit", "Carpool occasionally", "Drive a bit slower", "Use cruise control"],
		"answer": "Switch from car to public transit",
		"tags": ["transport", "emissions"],
		"difficulty": "medium",
		"points": 1,
	},

	"forest_1": {
		"title": "Deforestation Impact",
		"question": "List one major ecological consequence of large-scale deforestation.",
		"options": ["Loss of habitat", "Improved air quality", "Stronger storms", "Reduced carbon emissions"],
		"answer": "Loss of habitat",
		"tags": ["forests", "biodiversity", "climate"],
		"difficulty": "medium",
		"points": 1,
	},

	"pollution_1": {
		"title": "Air Quality",
		"question": "Which pollutant is especially associated with vehicle exhaust and can harm respiratory health?",
		"options": ["Sulfur dioxide (SO2)", "Nitrogen oxides (NOx)", "Chlorofluorocarbons (CFCs)", "Lead (Pb)"],
		"answer": "Nitrogen oxides (NOx)",
		"tags": ["air", "pollution"],
		"difficulty": "medium",
		"points": 1,
	},

	"plastic_1": {
		"title": "Single-Use Plastic",
		"question": "Which single-use plastic item is one of the top contributors to ocean plastic pollution?",
		"options": ["Plastic bags", "Plastic straws", "Reusable bottles", "Plastic cutlery"],
		"answer": "Plastic bags",
		"tags": ["plastic", "marine"],
		"difficulty": "easy",
		"points": 1,
	},

	"soil_1": {
		"title": "Soil Health",
		"question": "Why is maintaining healthy soil important for agriculture and climate?",
		"options": ["Stores carbon", "Kills plants", "Increases flooding", "Creates heat islands"],
		"answer": "Stores carbon",
		"tags": ["soil", "agriculture"],
		"difficulty": "medium",
		"points": 1,
	},

	"urban_1": {
		"title": "Urban Green Spaces",
		"question": "Name one benefit of urban green spaces for human communities.",
		"options": ["Heat reduction", "Improved air quality", "More traffic", "Less green cover"],
		"answer": "Heat reduction",
		"tags": ["urban", "ecosystem services"],
		"difficulty": "easy",
		"points": 1,
	},

	"invasive_1": {
		"title": "Invasive Species",
		"question": "What is a common ecological problem caused by invasive species?",
		"options": ["Outcompeting native species", "Boosting local crops", "Increasing native biodiversity", "Stabilizing habitats"],
		"answer": "Outcompeting native species",
		"tags": ["invasive", "biodiversity"],
		"difficulty": "medium",
		"points": 1,
	},

	"consumption_1": {
		"title": "Sustainable Consumption",
		"question": "Which consumer habit most directly reduces resource use and waste?",
		"options": ["Buying less new stuff", "Changing brands frequently", "Buying more packaged goods", "Upgrading devices yearly"],
		"answer": "Buying less new stuff",
		"tags": ["consumption", "circular economy"],
		"difficulty": "easy",
		"points": 1,
	},

	"food_1": {
		"title": "Food Waste",
		"question": "Which practice helps reduce household food waste?",
		"options": ["Meal planning", "Buying more perishable items", "Throwing leftovers away", "Overstocking pantry"],
		"answer": "Meal planning",
		"tags": ["food", "waste"],
		"difficulty": "easy",
		"points": 1,
	},

	"energy_2": {
		"title": "Home Efficiency",
		"question": "Which improvement typically yields large home energy savings?",
		"options": ["Switching to LED lighting", "Painting walls white", "Using incandescent bulbs", "Leaving windows open in winter"],
		"answer": "Switching to LED lighting",
		"tags": ["energy", "efficiency"],
		"difficulty": "easy",
		"points": 1,
	},

	"wetland_1": {
		"title": "Wetland Benefits",
		"question": "List one ecosystem service provided by wetlands.",
		"options": ["Flood mitigation", "Water filtration", "Biodiversity habitat", "Urban development"],
		"answer": "Flood mitigation",
		"tags": ["wetlands", "ecosystem services"],
		"difficulty": "medium",
		"points": 1,
	},

	"species_1": {
		"title": "Endangered Species",
		"question": "Name one primary driver of species becoming endangered.",
		"options": ["Habitat loss", "Overexploitation", "Pollution", "Climate change"],
		"answer": "Habitat loss",
		"tags": ["conservation", "species"],
		"difficulty": "medium",
		"points": 1,
	},

	"citizen_1": {
		"title": "Citizen Science",
		"question": "How can ordinary citizens contribute to environmental science?",
		"options": ["Reporting wildlife sightings", "Participating in local surveys", "Monitoring air or water quality", "Ignoring environmental issues"],
		"answer": "Reporting wildlife sightings",
		"tags": ["citizen science", "engagement"],
		"difficulty": "easy",
		"points": 1,
	},
}

__all__ = ["CHALLENGES"]

