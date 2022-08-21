import subprocess

def generate_sam_fasta(output_fasta_filename):
  subprocess.call(['samtools', 'faidx', output_fasta_filename])  

def generate_bwa_fasta(output_fasta_filename):  
  subprocess.call(['bwa', 'index', output_fasta_filename])  	
  
def generate_sam_fasta_dict(output_fasta_filename, output_fasta_dict_filename):  
  subprocess.call(['samtools', 'dict', output_fasta_filename, '-o', output_fasta_dict_filename])
  
def generate_bam(output_bam_sorted, output_RG_bam_sorted):
  gatk_rg = subprocess.call(['gatk', 'AddOrReplaceReadGroups', '--INPUT', output_bam_sorted, '--OUTPUT', output_RG_bam_sorted, '--RGLB', 'lib1', '--RGPL', 'illumina', '--RGPU', 'unit1', '--RGSM', '"CONTIG_ID"'])
  
def generate_vcf(row, output_phased_vcf, nucmer_pair_dfs, output_bam_sorted):
  subprocess.call(['whatshap', 'polyphase', '--ignore-read-groups', '--ploidy', str(row['estimated_ploidy']), '-o', output_phased_vcf, '--reference={}'.format(row['fasta_files']), nucmer_pair_dfs['HaplotypeCaller_VCFs'], output_bam_sorted])


    
