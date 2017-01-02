# geodjango-gis-map
//matricule : n:F74027078
/*Simple example using geodjango, postGis, leaflet, and displaying maps*/
at url ~/index , user can choose a country, and the mode to display:
  -displays urban areas in selected country
  -displays administrative borders intersecting the country border
  -displays list of airports in country
  -displays the area englobing the country


Data to fill the models can be load by launching the run() in the load files ( on for each model):
ex:
  // dont forget to create postGis dd, then:
  ./manage.py makemigrations
  ( You can verify migration files sql in the migration folder of the app)
  ./manage.py migrate
  ./manage.py shell
  >>from world import load_<model_name>
  >>run()
  
 Other informations:
    all models are in SRID=4326
  
