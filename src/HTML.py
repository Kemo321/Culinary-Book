def to_HTML(recipe):
    imageUrl = recipe['recipe']['image']
    calories = recipe['recipe'].get('calories', 'N/A')
    totalTime = recipe['recipe'].get('totalTime', 'N/A')
    nutrients = recipe['recipe']['totalNutrients']
    protein = nutrients.get('PROCNT', {'quantity': 0, 'unit': 'g'})
    fat = nutrients.get('FAT', {'quantity': 0, 'unit': 'g'})
    carbohydrates = nutrients.get('CHOCDF', {'quantity': 0, 'unit': 'g'})
    sugars = nutrients.get('SUGAR', {'quantity': 0, 'unit': 'g'})
    fiber = nutrients.get('FIBTG', {'quantity': 0, 'unit': 'g'})
    salt = nutrients.get('NA', {'quantity': 0, 'unit': 'mg'})

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 20px;
                padding: 0;
                background-color: #f4f4f4;
            }}
            h1 {{
                color: #333;
            }}
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 0 auto 20px;
            }}
            h2 {{
                color: #666;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 5px 0;
                padding: 5px;
                background-color: #fff;
                border-radius: 5px;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px;
                background-color: #007bff;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>{recipe['recipe']['label']}</h1>
        <img src='{imageUrl}' />
        <p>Calories: {calories:.2f}</p>
        <p>Preparation Time: {totalTime} minutes</p>
        <h2>Nutritional Information</h2>
        <ul>
            <li>Protein: {protein['quantity']:.2f} {protein['unit']}</li>
            <li>Fat: {fat['quantity']:.2f} {fat['unit']}</li>
            <li>Carbohydrates: {carbohydrates['quantity']:.2f} {carbohydrates['unit']}</li>
            <li>Sugars: {sugars['quantity']:.2f} {sugars['unit']}</li>
            <li>Fiber: {fiber['quantity']:.2f} {fiber['unit']}</li>
            <li>Salt: {salt['quantity']:.2f} {salt['unit']}</li>
        </ul>
        <h2>Ingredients</h2>
        <ul>
    """
    for ingredient in recipe['recipe']['ingredientLines']:
        html_content += f"<li>{ingredient}</li>"
    html_content += f"""
        </ul>
        <a href='{recipe['recipe']['url']}'>Link to recipe</a>
    </body>
    </html>
    """
    return html_content