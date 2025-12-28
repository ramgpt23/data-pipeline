# data-pipeline

A small end-to-end data pipeline that extracts video IDs, downloads transcripts, transforms the data, and generates text embeddings.

## Overview

The pipeline is implemented in `data_pipeline.py` and delegates work to `functions.py`. It runs four main steps in sequence and prints timing information for each step:

1. Extract video IDs (`getVideoIDs`) — collects or updates the list of video IDs to process.
2. Extract transcripts (`getVideoTranscripts`) — downloads transcripts for the collected video IDs and stores them in the `data/` folder.
3. Transform data (`transformData`) — applies cleaning/normalization and prepares a single dataset used for embedding.
4. Generate text embeddings (`createTextEmbeddings`) — converts cleaned text into embeddings for downstream tasks.

## Repository structure

- `data_pipeline.py` — main orchestration script that runs the four steps.
- `functions.py` — implementations for each pipeline step (see the file for details and configuration options).
- `requirements.txt` — Python dependencies to install.
- `data/` — storage for intermediate and final data files, for example:
  - `video-ids.parquet` — extracted video IDs
  - `video-index.parquet` - index videos
  - `video-transcripts.parquet` — downloaded transcripts

## Requirements

- Python 3.8+ recommended
- Install dependencies:

```powershell
pip install -r requirements.txt
```

Check `functions.py` for additional setup such as API keys or environment variables required to download transcripts or to call an embeddings service.

## How to run

From the `pipeline` folder run:

```powershell
python data_pipeline.py
```

The script prints start/end timestamps and the time taken for each step. Outputs are written to the `data/` directory; inspect `functions.py` for exact filenames and formats.

## Customization

- To change what youtube channel videos to be searched edit `channel_id` in `getVideoIDs` in `functions.py`
- To change what videos are fetched or how transcripts are downloaded, edit `getVideoIDs` and `getVideoTranscripts` in `functions.py`.
- To modify data cleaning or feature extraction, edit `transformData`.
- To change the embedding model or storage location for embeddings, edit `createTextEmbeddings`.

## Troubleshooting

- If the pipeline fails while downloading transcripts, verify network access and any API credentials required by the downloader implementation in `functions.py`.
- If a step is slow, check the printed timing messages to identify which step is the bottleneck.

## License

See the `LICENSE` file for license information.
