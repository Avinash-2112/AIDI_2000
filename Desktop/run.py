import subprocess

# Start the Streamlit app (frontend)
streamlit_cmd = "streamlit run frontend.py"
subprocess.Popen(streamlit_cmd, shell=True)

# Start the Flask app (backend)
flask_cmd = "python main.py"
subprocess.Popen(flask_cmd, shell=True)
