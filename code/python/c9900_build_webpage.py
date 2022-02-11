import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import requests

from c0001_retrieve_meta import retrieve_path




def build_webpage():
    """
    Objective: Summarize the projects and findings

    Tasks:
        1. Write summary of html

    """

    print("running build_webpage")

    tasks = [1]

    if 1 in tasks: introduction_html()


    print("completed build_webpage")



def introduction_html():
    """

    """

    h0_str = 'How many years of research do NIH awards support?'
    h0_txt = 'Motivation: Do researchers have time between applications to do work?'

    h1_str = 'Introduction'
    h1_txt = 'Queried the NIH Reporter archive to analyze the years of support provided by NIH awards. '


    index_html = retrieve_path('index_html')
    f = open(index_html, "w")
    f.close()
    f = open(index_html, "w")
    f.close()

    f = open(index_html, "w")
    f.write('<!DOCTYPE html>' + '\n' )
    f.write('<html>' + '\n' )
    f.write('<title>SupportYears</title>' + '\n' )
    f.write('</head>' + '\n' )

    f.write('<style>' + '\n' )
    f.write('.container {' + '\n' )
    f.write('width: 100%;' + '\n' )
    f.write('height: 100%;' + '\n' )
    f.write('}' + '\n' )
    f.write('img {' + '\n' )
    f.write('width: 80%;' + '\n' )
    f.write('height: 80%;' + '\n' )
    f.write('object-fit: cover;' + '\n' )
    f.write('}' + '\n' )
    f.write('</style>' + '\n' )



    # plot of the number of patents per year
    f.write('<body>' + '\n')
    f.write('<center>' + '\n')
    f.write('<div class="container">')

    f.write('<h1>' + str(h0_str) + '</h1>' + '\n')
    f.write('<p>' + str(h0_txt) + '</p>' + '\n')
    f.write('</body>' + '\n')

    f.write('<h2>' + str('Motivation') + '</h2>' + '\n')
    f.write('<p>' + str('Do researchers have time to do their work?' ))


    f.write('<h2>' + str('Objective') + '</h2>' + '\n')
    f.write('<p>' + str('Count how many years of research NIH supports for cell therapies using mesenchymal stem cells.' ))


    f.write('<h2>' + str('Tasks') + '</h2>' + '\n')
    f.write(str('The tasks to complete are: ') + '\n')
    f.write('</p>' + '\n')

    f.write(str('<ol>'))

    f.write('\n' + str('<li>'))
    f.write('\n' + str(' Query data (Manual)'))
    f.write('\n' + str('</li>'))

    f.write('\n' + str('<li>'))
    f.write('\n' + str(' Aggregate & clean'))
    f.write('\n' + str('</li>'))

    f.write('\n' + str('<li>'))
    f.write('\n' + str('  Plot'))
    f.write('\n' + str('</li>'))

    f.write('\n' + str('<li>'))
    f.write('\n' + str(' Make table'))
    f.write('\n' + str('</li>'))

    f.write('\n' + str('<li>'))
    f.write('\n' + str(' Build webpage'))
    f.write('\n' + str('</li>'))

    f.write('\n' + str(''))
    f.write(str('</ol>)'))

    f.write('</body>' + '\n')
    f.write('</center>' + '\n')

    name_article = 'nih_awards'
    plot_unique = str(name_article + '_unique_plot')
    name_unique = str(name_article + '_unique')

    for file in os.listdir(retrieve_path(plot_unique)):

        if 'Support Year' not in file:
            continue

        plot_dst = os.path.join(retrieve_path(plot_unique), file)

        f.write('<div>')
        f.write('<body>' + '\n')
        f.write('<center>' + '\n')

        # Insert static image of the current map
        f.write('<img alt="My Image" src="' + '')
        f.write(str(plot_dst))
        f.write('" />')

        f.write('</center>' + '\n')
        f.write('</body>' + '\n')
        f.write('</div>')
        f.close()

        for df_file in  os.listdir(retrieve_path(name_unique)):

            df_file_split = df_file.split('.')
            file_split = file.split('.')

            if file_split[0] == df_file_split[0]:

                df_file = os.path.join(retrieve_path(name_unique), file_split[0] + '.csv')
                print('build webpage: file for making into table : df_file = ' + str(df_file))

                write_table_count(df_file)

                """
                try:
                    write_table_count(file_path)
                except:
                    print('table skipped')
                """

    f = open(index_html, "a")

    """
    f.write('<body>' + '\n')
    f.write('<h1>' + str(h1_str) + '</h1>' + '\n')
    f.write('<p>' + str(h1_txt) + '</p>' + '\n')
    f.write('</body>' + '\n')
    """

    f.close()


    # Close the html file
    f = open(index_html, "a")
    f.write('</html>' + '\n' )
    f.close()


def write_table_count(file_path):
    """

    """

    print('file_path = ')
    print(file_path)

    file_split = file_path.split('/')
    file_name = file_split[-1]
    file_split = file_name.split('.')
    file_name = file_split[0]

    # retrieve trial counts
    df = pd.read_csv(file_path)
    del df['Unnamed: 0']

    print('df = ')
    print(df)

    df['counts'] = df['counts'].astype(int)

    df = df.sort()

    term = list(df['terms'])
    count = list(df['counts'])

    chart_title = 'Trial counts for the metadata term:' + file_name

    index_html = retrieve_path('index_html')
    f = open(index_html, "a")

    f.write('<body>' + '\n')
    f.write('<center>' + '\n')
    f.write('<h3>' + str(chart_title) + '</h3>' + '\n')
    f.write('<table>' + '\n')

    f.write('<tr>' + '\n')
    f.write('<th>' + file_name + '        ' + '</th>' + '\n')
    f.write('<th>' + 'Number of Patents' + '</th>' + '\n')
    f.write('</tr>' + '\n')

    for i in range(len(term)):

        print('i = ' + str(i))

        #if count[i] < 50: continue

        f.write('<tr>' + '\n')
        f.write('<th>' + str(term[i]) + '</th>' + '\n')
        f.write('<th>' + str(count[i]) + '</th>' + '\n')
        f.write('</tr>' + '\n')

    f.write('</table>' + '\n')
    f.write('</center>' + '\n')
    f.write('</body>' + '\n')
    f.close()




if __name__ == "__main__":
    main()
