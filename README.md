# mapred-hadoop

Unzip `timeline.zip` to get `timeline.json`.

Then, upload `timeline.json` to Hadoop: `hadoop fs -put timeline.json /path`

For every task, `time` will be called to obtain the total time used.

- Baseline: `time cat timeline.json | sum.py`
- MapReduce (local): `time cat timeline.json | python3 mapper2.py | python3 reducer.py
- MapReduce (Hadoop): `time mapred streaming -files mapper2.py,reducer.py -input /path/timeline.json -output output_name -mapper "python3 mapper2.py" -reducer "python3 reducer.py"`
- MapReduce (modified task) (local): `time cat timeline.json | python3 mapper.py | python3 reducer.py
- MapReduce (modified task) (Hadoop): `time mapred streaming -files mapper.py,reducer.py -input /path/timeline.json -output output_name -mapper "python3 mapper.py" -reducer "python3 reducer.py"`
- mrjob (local): `time python3 sum_mrjob.py timeline.json -o mrjob_results`
- mrjob (Hadoop): `time python3 sum_mrjob.py -r hadoop hdfs:///path/timeline.json -o hdfs:///path_to_output/`
