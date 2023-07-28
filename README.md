# mapred-hadoop

**Assignment for IST3134**

Unzip `timeline.zip` to get `timeline.json`.

Then, upload `timeline.json` to Hadoop: `hadoop fs -put timeline.json /path`

For every task, `time` will be called to obtain the total time used.

- Baseline: `time cat timeline.json | sum.py`
- MapReduce (local): `time cat timeline.json | python3 mapper2.py | python3 reducer.py`
- MapReduce (Hadoop): `time mapred streaming -files mapper2.py,reducer.py -input /path/timeline.json -output output_name -mapper "python3 mapper2.py" -reducer "python3 reducer.py"`
- MapReduce (modified task) (local): `time cat timeline.json | python3 mapper.py | python3 reducer.py`
- MapReduce (modified task) (Hadoop): `time mapred streaming -files mapper.py,reducer.py -input /path/timeline.json -output output_name -mapper "python3 mapper.py" -reducer "python3 reducer.py"`
- mrjob (local): `time python3 sum_mrjob.py timeline.json -o mrjob_results`
- mrjob (Hadoop): `time python3 sum_mrjob.py -r hadoop hdfs:///path/timeline.json -o hdfs:///path_to_output/`

***

**28 July update**

Because the MapReduce task runs slower on Hadoop, an experiment is conducted to examine the overhead of streaming a MapReduce job to a Hadoop cluster.

In the experiment, time delays are added into every line input of the mapper.

`experiment.sh` is used to run the experiment on local, and `experiment_hadoop.sh` is used to run it on Hadoop. Both results are compared.

`experiment_hadoop2.sh` is another test run for time delay = 500ms, as the time delays in the mentioned experiment are insufficient to see any changes in running time while running on Hadoop.
