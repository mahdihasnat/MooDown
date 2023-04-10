# MooDown
Moodle downloader

### Adding `.env` file

Add a `.env` file under the `src` directory

```ruby
baseurl=https://moodle.cse.buet.ac.bd/
moodle_id=1705010
moodle_pwd=YOUR_PASSWORD
local_output_dir=../tmp/
```

### Running Downloader

- `pip install -r requirements.txt`
- `python src/main.py`
- Current progress is saved in `src/q.pickle` and `src/visited.pickle` file. To parse from the beginning, delete these files.