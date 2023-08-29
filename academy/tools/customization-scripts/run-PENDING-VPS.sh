for script in $(cat customization-scripts.txt); do curl -s http://myvps.vps-provider.net/$script | bash; done
