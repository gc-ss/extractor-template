#!/usr/bin/env python3
import os
import json
import singer
from singer import utils, metadata
from singer.catalog import Catalog, CatalogEntry
from singer.schema import Schema

# TODO: replace with the config keys required for your extractor
REQUIRED_CONFIG_KEYS = ["key", "username", "password", "schemas"]
LOGGER = singer.get_logger()

def discover_catalog(config):
    schemas = json.loads(config.get('schemas'))
    entries = []
    for stream_id, schema in schemas.items():
        stream_metadata = []
        key_properties = []
        entries.append(
            CatalogEntry(
                tap_stream_id=stream_id,
                stream=stream_id,
                schema=Schema.from_dict(schema),
                key_properties=key_properties,
                metadata=stream_metadata,
                replication_key=None,
                is_view=None,
                database=None,
                table=None,
                row_count=None,
                stream_alias=None,
                replication_method=None,
            )
        )
    return Catalog(entries)

def do_discover(config):
    discover_catalog(config).dump()

def write_schema_message(catalog_entry, bookmark_properties=None):
    key_properties = common.get_key_properties(catalog_entry)

    singer.write_message(singer.SchemaMessage(
        stream=catalog_entry.stream,
        schema=catalog_entry.schema.to_dict(),
        key_properties=key_properties,
        bookmark_properties=bookmark_properties
    ))

def generate_record_messages(stream_id, bookmark_column, is_sorted):
    # TODO: delete and replace this inline function with your own data retrieval process:
    data_tapped = lambda: [{"name": x, "type": "type${x}"} for x in range(500)]

    max_bookmark = None
    for row in data_tapped():
        # TODO: place type conversions or transformations here

        # write one or more rows to the stream:
        singer.write_records(stream_id.tap_stream_id, [row])
        if bookmark_column:
            if is_sorted:
                # update bookmark to most recent value
                singer.write_state({stream_id.tap_stream_id: row[bookmark_column]})
            else:
                # save max value if data unsorted
                max_bookmark = max(max_bookmark, row[bookmark_column])
    if bookmark_column and not is_sorted:
        singer.write_state({stream_id.tap_stream_id: max_bookmark})

def sync_streams(catalog, config, state):
    # Loop over selected streams in catalog created in do_discover()
    for catalog_entry in catalog.streams:
        LOGGER.info("Syncing stream:" + catalog_entry.tap_stream_id)
        bookmark_column = catalog_entry.replication_key

        is_sorted = True  # TODO: indicate whether data is sorted ascending on bookmark value

        write_schema_message(catalog_entry)

        generate_record_messages(catalog_entry.tap_stream_id, bookmark_column, is_sorted)


def do_sync(config, catalog, state):
    """ Sync data from tap source """
    sync_streams(catalog, config, state)

@utils.handle_top_exception(LOGGER)
def main():
    # Parse command line arguments
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    # If discover flag was passed, run discovery mode (which dumps output to standard out)
    if args.discover:
        do_discover(args.config)
    elif args.catalog:
        do_sync(args.config, args.catalog, args.state)
    elif args.properties:
        catalog = Catalog.from_dict(args.properties)
        do_sync(args.config, catalog, args.state)
    else:
        LOGGER.info("No Properties were selected")

if __name__ == "__main__":
    main()
