*please see the README.md at the root of this project for more general instructions*

##OS X Setup#

These are examples of how to configre this to function on an OS X Mountian Lion Server (it should also work for Lion)
It uses the webappctl control, but can also be used with the server app.


this project was forked with the intention of running on sub-path of /crypt (eg http://your.server.com/crypt)
and that is represented in the included httpd_crypt.conf file with the WSGIScriptAlias line

	WSGIScriptAlias /crypt */path/to/your/*crypt_env/crypt/crypt.wsgi


the other primary change in this fork was to allow for multiple django-wsgi apps to be run side-by side hence the renaming of /static/ directive in the settings.py file to /static_crypt/.  With that set you can Alias more than one set of static files properly.

	Alias /static_crypt/ */path/to/your/*crypt_env/crypt/static_crypt/

####To install (on 10.8 )####
Edit crypt.wsgi specifiying your virtualenv directory and place in 

	*/path/to/your/*crypt_env/crypt/

Now edit the httpd_crypt.conf specifying the location of where you just placed the crypt.wsgi file, and place that file in

	/Library/Server/Web/Config/apache2/ **

and finally edit the the com.grahamgilbert.crypt.plist specifying the location of where you placed crypt.wsgi, and place that file in

	/Library/Server/Web/Config/apache2/webapps/ **

#######** if you've changed the "service data location" using the server app make the proper adjustments to the path.