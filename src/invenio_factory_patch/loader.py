def _loader(app, init_func, entry_points=None, modules=None):
    """Run generic loader.
    
        Used to load and initialize entry points and modules using an custom
        initialization function.
    
        .. versionadded: 1.0.0
        """
    if entry_points:
        for group in entry_points:
            for ep in entry_points[group]:
                try:
                    init_func(ep.load())        
                except Exception:
                    app.logger.error(f"Failed to initialize entry point: {ep}")
                    raise
    if modules:
        for m in modules:
            try:
                init_func(m)
            except Exception:
                app.logger.error(f"Failed to initialize module: {m}")
                raise


def app_loader(app, entry_points=None, modules=None):
    _loader(app, lambda ext: ext(app), entry_points=entry_points, modules=modules)
            
