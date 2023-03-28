import os
import sys
import pandas as pd
import re
from lookups import LA_CODES
from util import slugify, load_data, filtering, path_name, drop_totals

if __name__ == '__main__':

    # specify filepath
    filepath = 'data/csv/fe_dest/16-18 local authority level destinations.csv'
    group = sys.argv[1]

    data = load_data(filepath, group=group, fill_na=True, value=2)
    SEN_data = data.drop(columns= ['institution_group', 'cohort_level', 'institution_type'])
    data = data[data.institution_group == 'State-funded mainstream schools & colleges'].drop(columns=
    ['institution_group', 'cohort_level', 'institution_type'])
    data = data[data.data_type != 'Percentage'].drop(columns=['data_type'])

    for i in ['fe_level_3', 'fe_level_2', 'fe_entry_level_and_no_identified_level', 'other_education_destinations']:
        filtered_data = filtering(
            data, facts=i, dat='2020/21', subfilts=['characteristic_group', 'student_characteristic'])

        path = path_name(facts=i, subfilts=['characteristic_group', 'student_characteristic'],
                         dat='2020/21', group=group, stage='fe_dest')
        
        # write to file
        filtered_data.to_csv(path)

    # for i in ['fe_level_3']:
    #     filtered_SEN_data = filtering(
    #         SEN_data, facts=i, dat='2020/21', subfilts=['characteristic_group', 'student_characteristic'])
    #         filtered_SEN_data = filtered_SEN_data.loc[["LLDD Provision", "SEN Provision"]].drop(columns=['Disadvantaged', 'Female', 'Male', 'Not Disadvantaged'])
    #@TODO find way to merge with above to avoid wriitng to separate file.
    


    #@TODO add code below to get visualisations for people going on to apprenticeships at levels 2, 3, 4. 
    # for i in ['higher_and_degree_apprenticeships_level_4_and_above', 'advanced_apprenticeships_level_3', 'intermediate_apprenticeships_level_2']:
    #     filtered_data = filtering(
    #         data, facts=i, dat='2020/21', subfilts=['characteristic_group', 'student_characteristic'])

    #     path = path_name(facts=i, subfilts=['characteristic_group', 'student_characteristic'],
    #                      dat='2020/21', group=group, stage='fe_dest')
        
    #     # write to file
    #     filtered_data.to_csv(path)
