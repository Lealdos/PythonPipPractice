import matplotlib.pyplot as plt

def generate_bar_chart(name: str,labels:float, values:int):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(f'{name}', fontsize=10)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(region:str,labels:float, values:int):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{region}.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    # generate_bar_chart(name,labels, values)
    # generate_pie_chart(labels, values)
    #Final test
