#!/usr/bin/env python

import pandas as pd
from django.template import Template, Context, loader
from django.conf import settings
settings.configure()

mep_df = pd.read_csv('clean_output.csv')
mep_full_data = mep_df.to_dict('r')

# print mep_full_data

# mep_img_urls_df = pd.read_csv('mep_prof_img_url.csv')
# mep_img_data = mep_img_urls_df.to_dict('r')

# print mep_img_data


template = """
{% for mep_row in mep_data %} 
	<div class="portfolio {{ mep_row.NAME|make_list|first }}" data-cat="{{ mep_row.NAME|make_list|first }}">
    	<div class="portfolio-wrapper">
    		<a href="pages/{{ mep_row.SCREEN_NAME }}.html"><img width="300" height ="200" src="{{ mep_row.prof_img_url }}" alt="{{ mep_row.NAME }}" /></a>
        		<div class="label">
            		<div class="label-text">
               			 <a class="text-title">{{ mep_row.NAME }}</a>
                			<span class="text-category"> {{ mep_row.NATIONALITY }} </span>
            		</div>
            		<div class="label-bg"></div>
        		</div>
    	</div>
	</div>
	
{% endfor %}
"""

t = Template(template)
c = Context({"mep_data": mep_full_data})

f1=open('index_divs.html', 'w+')
try:
	f1.write(t.render(c).encode('utf-8'))
except UnicodeEncodeError:
	f1.write(t.render(c).encode('ascii', 'ignore').decode('ascii'))

f1.close()