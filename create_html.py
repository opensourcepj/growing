from jinja2 import Environment, PackageLoader, select_autoescape
import os
import random

task_list = [
"Plant",
"Sow",
"Irrigate",
"Til"
]


output_list = [
{
'vegetable': 'asparagus',
'img':os.path.join('img','asparagus.jpg'),

'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)
},
{
'vegetable': 'brocolli',
'img':os.path.join('img','brocolli.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'brussels-sprout',
'img':os.path.join('img','brussels-sprouts.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'cabbage',
'img':os.path.join('img','cabbage.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)


},
{
'vegetable': 'carrot',
'img':os.path.join('img','carrot.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'cauliflower',
'img':os.path.join('img','cauliflower.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'celery',
'img':os.path.join('img','celery.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'cucumber',
'img':os.path.join('img','cucumber.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'green bean',
'img':os.path.join('img','green_bean.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'kale',
'img':os.path.join('img','kale.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'lettuce',
'img':os.path.join('img','lettuce.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'onion',
'img':os.path.join('img','onion.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'parsnip',
'img':os.path.join('img','parsnip.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'pea',
'img':os.path.join('img','pea.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'potato',
'img':os.path.join('img','potato.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'scallion',
'img':os.path.join('img','scallion.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'spinach',
'img':os.path.join('img','spinach.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'tomato',
'img':os.path.join('img','tomato.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

},
{
'vegetable': 'turnip',
'img':os.path.join('img','turnip.jpg'),
'other_growers_area': random.randrange(1,10),
'other_growers_connections': random.randrange(1,10),
'number_of_comments': random.randrange(1,10),
'growing_percentage':random.randrange(1,100,1),
'hours_percentage':random.randrange(1,100,1),
'growing_estimate':random.randrange(50,100,1),
"next_task": task_list[random.randrange(1,3)],
"next_task_time": random.randrange(1,10),
'hours_estimate':random.randrange(50,100,1),
'size': random.randrange(10,100,10),
'output_estimate': random.randrange(10,100,10),
"value_estimate": random.randrange(10,100,10)

}
]


env = Environment(
    loader=PackageLoader('create_html', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template1.html')

with open('index.html', 'w') as f:
    f.write(template.render(output_list=output_list))
