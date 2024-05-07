import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget


def create_chart():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart
    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0"
                    }
                },

                "fontSize": 10
            },
        )
    )

    chart.animate(
        Config.stackedColumn(
            {
                "x": "Count",
                "y": "new lead time Range",
                "label": "booking status",
                "legend": "color",

            }
        )
    )

    chart.animate(
        Config(
            {
                "x": ["Count", "booking status"],
                "label": ["Count"],
                "color": "booking status",
            }
        )
    )

    chart.animate(Config({"x": "Count", "y": ["new lead time Range", "booking status"]}))

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()


def create_chart2():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart

    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0"
                    }
                },
                "fontSize": 10,
            }
        )
    )

    chart.animate(Config({"x": "Count", "y": ["booking status"]}))

    chart.animate(
        Config.pie(
            {
                "angle": "Count",
                "by": "booking status",
                "title": "",
            }
        )
    )

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()


def create_chart3():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    # Belirtilen değerler dışındaki satırları droplama
    valid_values = ['Free', 'Less than 50', '50 - 100', '100 - 199', '200 and above']
    df = df[df['new Average Price Range'].isin(valid_values)]

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart

    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0 #C2471C #382258 #6E6344"
                    }
                },
                "fontSize": 10,
            }
        )
    )

    chart.animate(
        Config.radialBar(
            {
                "angle": "Count",
                "radius": "new Average Price Range",
                "title": "",
            }
        )
    )

    chart.animate(
        Config.percentageColumn(
            {
                "x": "new Average Price Range",
                "y": "Count",
                "stackedBy": "booking status",
                "title": "",
            }
        )
    )

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()


def create_chart4():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart

    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0 #C2471C #382258 #6E6344"
                    }
                },
                "fontSize": 10,
            }
        )
    )

    chart.animate(
        Config.stackedBubble(
            {
                "size": "Count",
                "color": "new guest type",
                "stackedBy": "booking status",
                "title": "",
            }
        )
    )

    chart.animate(
        Config.percentageColumn(
            {
                "x": "new guest type",
                "y": "Count",
                "stackedBy": "booking status",
                "title": "",
            }
        )
    )

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()


def create_chart5():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    df['date of reservation'] = pd.to_datetime(df['date of reservation'])

    # Ay bilgisini içeren 'Month' sütununu oluşturalım
    df['Month'] = df['date of reservation'].dt.month

    # Ay bilgisini isimlere dönüştürelim
    df['Month'] = df['Month'].map(
        {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
         9: 'September', 10: 'October', 11: 'November', 12: 'December'})

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart

    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0 #C2471C #382258 #6E6344"
                    }
                },
                "fontSize": 10,
            }
        )
    )

    chart.animate(
        Config.stackedColumn(
            {
                "x": "Month",
                "y": "Count",
                "label": "booking status",
                "legend": "color",

            }
        )
    )

    chart.animate(
        Config(
            {
                "x": ["Month", "booking status"],
                "label": "Count",
                "color": "booking status",
            }
        )
    )

    chart.animate(Config({"x": ["Month", "booking status"], "y": "Count"}))

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()


def create_chart6():
    # initialize Chart

    chart = Chart(
        width="640px", height="360px", display=DisplayTarget.MANUAL
    )

    # create and add data to Chart

    data = Data()
    df = pd.read_csv(
        "data/new_booking2.csv"
    )

    df['booking status'] = df['booking status'].replace({0: 'Not Cancel', 1: 'Canceled'})

    df['Count'] = 1

    data.add_df(df)

    chart.animate(data)

    # add config to Chart

    chart.animate(
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#56AEFF #145DA0 #C2471C #382258 #6E6344"
                    }
                },
                "fontSize": 10,
            }
        )
    )

    chart.animate(Config({"x": "Count", "y": ["market segment type"]}))

    chart.animate(
        Config.nestedDonut(
            {
                "angle": "Count",
                "stackedBy": "market segment type",
                "radius": "booking status",
                "title": "",
            }
        ),
        Style(
            {
                "plot": {
                    "marker": {
                        "rectangleSpacing": "0",
                        "borderWidth": 1,
                        "borderOpacity": 0,
                    }
                }
            }
        ),
    )

    # Add style to Chart
    style = Style(
        {
            "title": {"fontSize": "35px"},
        }
    )
    chart.animate(style)

    # return generated html code

    return chart._repr_html_()

