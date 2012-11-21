import os, sys, logging
import ConfigParser

def main():
    config = ConfigParser.ConfigParser()

    try:
        config.readfp(open('interceptor_config.ini'))
        
        log_file = config.get('system', 'log')
        if log_file is not None:
            logging.basicConfig(level=logging.DEBUG, filename=log_file)
        else:
            logging.basicConfig(level=logging.DEBUG)

        i = dict(config.items('apps'))
        logging.info("Configured apps: %s" % i.keys())
        pname = sys.argv[0]
        if not i.has_key(pname):
            logging.error("Unknown app %s, check config file" % pname)
            logging.error("argv: %s" % sys.argv[1:])
            return
        logging.info("Executing %s - argv: %s" % (i[pname], sys.argv))
        os.execv(i[pname], sys.argv)
    except Exception, e:
        logging.error("Error: %s" % e)

if __name__ == '__main__':
    main()
