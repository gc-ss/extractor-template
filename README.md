# extractor-template

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating
[Meltano](https://github.com/meltano) extractors.

## Usage

First, install cookiecutter:

```bash
$ pip install cookiecutter
```

Next, initialize your project. Provide the prompted information.

```bash
$ cookiecutter https://github.com/Qualytics/extractor-template
extractor_name [e.g. 'extract-facebook']: extract-bigquery
```

For the package_name, hit enter and the package name will match your provided extractor name.

```bash
package_name [extract_bigquery]:
```

Your project now exists. Next integrate with a Meltano project.

## Add to Meltano Project

First create a [Meltano Project](https://meltano.com/docs/getting-started.html#create-your-meltano-project).

Once you have your meltano project initialized, you are ready to add this extractor
as a custom extractor. To do this, run the following in your Meltano Project and
provide the prompted information:

```bash
$ meltano add --custom extractor <extractor-name>
(namespace): extract_bigquery
(pip_url): -e <project-directory-path>
(executable): extract-bigquery
(capabilities): catalog,discover,state
(settings): key,username,password
```

To edit your config variables, edit meltano.yml file found in your Meltano
project.

Now you can get to work on writing your extractor! See todo's in \_\_init\_\_.py. 

Copyright &copy; 2020 Qualytics
