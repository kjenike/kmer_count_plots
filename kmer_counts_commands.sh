for read_number in {001..100}
do
  num_lines=`expr $read_number \* 2`
  value=`head -n $num_lines fasta.fasta | tail -n 1`
  get_counts some_kmc_database $value >> COUNTS/counts"$read_number".txt
done
