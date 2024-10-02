
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv('cleaned_bert_topic.csv', encoding='utf-8-sig')
# Count the occurrences of each topic
topic_counts = df.groupby('Clustered Topic name')['Count'].sum()

# Create a pie chart
pie_fig = go.Figure(data=[go.Pie(labels=topic_counts.index, values=topic_counts.values)])
pie_fig.update_layout(title='Topic Distribution')

# Create a bar chart
bar_fig = px.bar(df, x='Clustered Topic name', y='Count', color='Topic', title='Topic Frequency Bar Chart')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("Topic Modelling Dashboard", style={'textAlign': 'center'}),
    
    # Pie chart
    html.Div(children=[
        dcc.Graph(figure=pie_fig)
    ], style={'width': '100%'}),
    
    # Bar chart
    html.Div(children=[
        dcc.Graph(figure=bar_fig)
    ], style={'width': '100%'}),
    
    # Images (assuming these are relevant visualizations or graphics)
    html.Div(children=[
        html.Img(src="/assets/MH.png", style={'width': '75%', 'height': 'auto'})
    ], style={'width': '75%', 'textAlign': 'center'}),
    
    html.Div(children=[
        html.Img(src="/assets/LURD.png", style={'width': '75%', 'height': 'auto'})
    ], style={'width': '75%', 'textAlign': 'center'}),
    
    html.Div(children=[
        html.Img(src="assets/sfc.png", style={'width': '75%', 'height': 'auto'})
    ], style={'width': '75%', 'textAlign': 'center'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)