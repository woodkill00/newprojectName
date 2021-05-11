import uuid, base64
from apps.customerApp.models import Customer
from apps.userApp.models import UserProfile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


def get_salesman_from_id(val):
    salesman = UserProfile.objects.get(id=val)
    return salesman

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(results_by):
    if results_by == '#1':
        key = 'transaction_id'
    elif results_by == '#2':
        key = 'created'
    return key

def get_chart(chart_type, data, results_by, **kwargs):
    plt.switch_backend('AGG')
    # setting size of the chart
    fig = plt.figure(figsize=(10,4))
    key = get_key(results_by)
    d = data.groupby(key, as_index=False)['total_price'].agg('sum')
    if chart_type == '#1':
        print('bar chart')
        # plt.bar(d[key], data['total_price'])
        sns.barplot(x=key, y='total_price', data=d)
    elif chart_type == '#2':
        print('pie chart')
        lables = kwargs.get('lables')
        plt.pie(data=d, x='total_price', labels=d[key].values)
        # plt.pie(data=data, x='price', lables=lables)
    elif chart_type == '#3':
        print('line chart')
        plt.plot(d[key], d['total_price'], color='green', marker='o', linestyle='dashed')
    else:
        print('failed to identify the chart type')
    # adjusts the size of the chart to the fig size stated above
    plt.tight_layout()
    chart = get_graph()
    return chart