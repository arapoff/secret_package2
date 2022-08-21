import subprocess

def some_function():
	## index them now
	subprocess.call(['samtools', 'faidx', output_fasta_filename])  
	subprocess.call(['bwa', 'index', output_fasta_filename])  	
	## also need samtools dict
	subprocess.call(['samtools', 'dict', output_fasta_filename, '-o', output_fasta_dict_filename])
  
  gatk_rg = subprocess.call(['gatk', 'AddOrReplaceReadGroups', '--INPUT', output_bam_sorted, '--OUTPUT', output_RG_bam_sorted, '--RGLB', 'lib1', '--RGPL', 'illumina', '--RGPU', 'unit1', '--RGSM', '"CONTIG_ID"'])
  
  subprocess.call(['whatshap', 'polyphase', '--ignore-read-groups', '--ploidy', str(row['estimated_ploidy']), '-o', output_phased_vcf, '--reference={}'.format(row['fasta_files']), nucmer_pair_dfs['HaplotypeCaller_VCFs'], output_bam_sorted])
