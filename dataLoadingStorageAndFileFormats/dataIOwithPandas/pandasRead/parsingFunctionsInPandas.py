'''
Table: The following are pandas methods to read from various file types.
They convert text data into a DataFrame.
============================================================================================
Function------------Description-------------------------------------------------------------
============================================================================================
read_csv            Load delimited data from a file, URL, or file-like obj; use comma as 
                    default delimiter
============================================================================================
read_fwf            Read data in fixed-width column format (i.e. no delimiters)
============================================================================================
read_clipboard      Version of read_csv that reads data from the clipboard; useful for 
                    converting tables from web pages.
============================================================================================
read_excel          Read tabular data from an Excel XLS or XLSX file
============================================================================================
read_hdf            Read HDF5 files written by pandas
============================================================================================
read_html           Read all tables found in the given HTML document
============================================================================================
read_json           Read data from a JSON string representation
============================================================================================
read_msgpack        Read pandas data encoded using the Message-Pack binary format
============================================================================================
read_pickle         Read an arbitrary object stored in Python pickle format
============================================================================================
read_sas            Read a SAS dataset stored in one of the SAS system's custom storage
                    formats
============================================================================================
read_sql            Read the results of a SQL query (using SQLAlchemy) as a pandas DataFrame
============================================================================================
read_stata          Read a dataset from the Stata file format
============================================================================================
read_feather        Read the Feather binary file format
============================================================================================
'''


'''
# In addition to using methods to indicate the file type being read, various optional arguments fall into the following categories:
============================================================================================
Category------------Description-------------------------------------------------------------
============================================================================================
Indexing            Can treat one or more columns as the returned DataFrame, and determines
                    whether to get column names from the file, the user, or not at all.
============================================================================================
Type Inference      This includes the user-defined value conversions and custom list of
and Data            missing value markers.
Conversion
============================================================================================
Datetime parsing    Includes combining capability, including combining date and time
                    information spread over multiple columns into a single column in the
                    result.
============================================================================================
Iterating           Support for iterating over chunks of very large files.
============================================================================================
Unclean data        Skipping rows or a footer, comments, or other minor things like numeric
issues              data with thousands separated by commas
============================================================================================
'''