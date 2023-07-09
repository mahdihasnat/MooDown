# MooDown
Moodle downloader

### Running MooDown
- Adding `.env` file
  - Add a `.env` file under the `src` directory. Contents of `.env` file is the following:
  - ```ruby
    baseurl=https://moodle.cse.buet.ac.bd/
    moodle_id=1705010
    moodle_pwd=YOUR_PASSWORD
    local_output_dir=../tmp/
    ```

- Install the requirements
  - ```bash
    pip install -r requirements.txt
    ```
- Run `main.py`
  - ```bash
    python src/main.py
    ```
### Note
- Current progress is saved in `src/q.pickle` and `src/visited.pickle` file. To parse from the beginning, delete these files.
