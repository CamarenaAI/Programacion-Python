def make_car(manafacturer, model, **car_info):
    """Build a dictionary containing everything we know a bout a car"""
    car_info['manafacturer'] = manafacturer
    car_info['model_name'] = model
    return car_info

car = make_car('toyota', 'corolla', color='gray', year='1970', hp='75')
print(car)

car = make_car('volkswagen', 'golf', color='black', year='1976', hp='170')
print(car)

car = make_car('ford', 'mustang', color='red', year='2020', hp='700')
print(car)