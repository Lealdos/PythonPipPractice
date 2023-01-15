import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    option = ', '.join(sorted(set(map(lambda i: i['Continent'],data ))))
    print('Continets: '+ option)
    region = input('Type Continet => ')
    data = list(filter(lambda item : item['Continent'] == f'{region}',data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(region,countries, percentages)
    option = ', '.join(sorted(set(map(lambda i: i['Country/Territory'],data ))))
    print(f"Countrys on {region} : {option}" )
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        name = country['Country/Territory']
        charts.generate_bar_chart(name,labels,values)



if __name__ == '__main__':
    run()
    