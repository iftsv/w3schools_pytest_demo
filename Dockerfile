FROM selenium/standalone-chrome
WORKDIR /tests_project/
RUN sudo apt update && sudo apt install -y git && \
    sudo apt install -y python3-pip && \
    curl https://raw.githubusercontent.com/iftsv/w3schools_pytest_demo/master/requirements.txt -o requirements.txt && \
    pip install -r requirements.txt
CMD rm -r * && \
    git clone --depth 1 https://github.com/iftsv/w3schools_pytest_demo.git . && \
    python3 -m pytest -s --alluredir=test_results/ ./tests/