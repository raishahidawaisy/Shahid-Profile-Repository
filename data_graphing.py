import csv

#final desired format > lets make it a list

raidboss_info = []
with open('raidboss_data.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        raidboss_info.append(row)

raidboss_details = [raidboss_info[0]]

for row in raidboss_info[1:]:
    boss_brigade_id = row[0]
    #if not row[1] or not row[2] or not row[3]:
    #    continue
    boss_hps = int(row[1])
    #boss_level = row[2]
    #boss_max_pts = row[3]
    #raidboss_details.append([boss_brigade_id,boss_hps,boss_level,boss_max_pts])
    raidboss_details.append([boss_brigade_id,boss_hps])

from string import Template

html_string = Template("""<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart (){
      var data = google.visualization.arrayToDataTable([
      $labels
      $data
      ],
      false); // 'false' means that the first row contains labels, not data.
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
    <div id="chart_div" style="width:1000; height:1000"></div>
</body>
</html>""")

chart_data_str = ''
for row in raidboss_details[1:]:
    chart_data_str += '%s,\n'%row

completed_html = html_string.substitute(labels=raidboss_details[0],data=chart_data_str)

with open('raidboss_detail.html','w') as f:
    f.write(completed_html)

print (raidboss_details)
print (len(raidboss_details))
