FROM mltooling/ml-workspace-minimal:0.12.1
RUN pip install plotly
RUN pip install streamlit



EXPOSE 8080