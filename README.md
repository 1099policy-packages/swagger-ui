## SwaggerUI Configuration

  You can configure Swagger parameters using the dictionary, Both key and value are of type str, if value is JavaScript string, you need to wrap the quotes around it.
  Such as `"layout": "\"StandaloneLayout\""`.

  ```python
  parameters = {
      "deepLinking": "true",
      "displayRequestDuration": "true",
      "layout": "\"StandaloneLayout\"",
      "plugins": "[SwaggerUIBundle.plugins.DownloadUrl]",
      "presets": "[SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset]",
  }
  SwaggerUI(app, config_path='./config/test.yaml', parameters=parameters)
  ```

  For details about parameters configuration, see the official documentation [Parameters Configuration](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/).

## OAuth2 Configuration

  The format is similar to `parameters`.

  ```python
  oauth2_config = {
      "clientId": "\"your-client-id\"",
      "clientSecret": "\"your-client-secret-if-required\"",
      "realm": "\"your-realms\"",
      "appName": "\"your-app-name\"",
      "scopeSeparator": "\" \"",
      "scopes": "\"openid profile\"",
      "additionalQueryStringParams": "{test: \"hello\"}",
      "usePkceWithAuthorizationCodeGrant": True,
  }
  SwaggerUI(app, config_path='./config/test.yaml', oauth2_config=oauth2_config)
  ```