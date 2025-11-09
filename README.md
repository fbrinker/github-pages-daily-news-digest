# Daily News Digest

**Work in Progress**

A daily news digest that curates the most important stories and articles from around the web and presents them on a Jekyll-based GitHub Pages website. Articles are updated daily and organized by various categories.

https://fbrinker.github.io/github-pages-daily-news-digest/

## Lokale Entwicklung mit Docker

Diese Jekyll-Site kann lokal mit Docker ausgeführt werden, ohne Jekyll lokal installieren zu müssen.

### Voraussetzungen

- Docker und Docker Compose müssen installiert sein

### Starten der lokalen Entwicklungsumgebung

1. **Mit Docker Compose (empfohlen):**
   ```bash
   docker-compose up
   ```

2. **Oder mit Docker direkt:**
   ```bash
   docker build -t jekyll-site .
   docker run -p 4000:4000 -v ${PWD}/docs:/srv/jekyll jekyll-site
   ```

Die Site ist dann unter `http://localhost:4000` erreichbar.

### Wichtige Hinweise

- Änderungen an den Dateien im `docs/` Verzeichnis werden automatisch erkannt und die Site wird neu generiert
- Um den Container zu stoppen, drücken Sie `Ctrl+C` oder führen Sie `docker-compose down` aus
- Bei Problemen können Sie den Container mit `docker-compose down` stoppen und mit `docker-compose up --build` neu starten