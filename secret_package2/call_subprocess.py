import subprocess

def call_bwa():
  subprocess.call(['bwa', 'index']) 
  subprocess.call(['samtools', 'faidx'])
  gatk_rg = subprocess.call(['gatk', 'AddOrReplaceReadGroups', '--INPUT', output_bam_sorted, '--OUTPUT', output_RG_bam_sorted, '--RGLB', 'lib1', '--RGPL', 'illumina', '--RGPU', 'unit1', '--RGSM', '"CONTIG_ID"'])
  subprocess.call(['whatshap', 'polyphase', '--ignore-read-groups', '--ploidy', str(row['estimated_ploidy']), '-o', output_phased_vcf, '--reference={}'.format(row['fasta_files']), nucmer_pair_dfs['HaplotypeCaller_VCFs'], output_bam_sorted])
