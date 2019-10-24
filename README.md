# Notes
Centralised project for learning Cloud and DevOps Topics (just getting started).
<!--TOC_START-->
## Contents
- [Repository Forking & Rebasing](#repository-forking--rebasing)
	- [Contributing](#contributing)
	- [Automation](#automation)
		- [Circle CI](#circle-ci)
		- [Local Setup](#local-setup)

<!--TOC_END-->
## Repository Forking & Rebasing
It's recommended to fork this repository to benefit from the examples and exercises.
To handle updates from this main repository on your forked one, you can rebase to update any changes:
1. Add this project as an upstream from your forked repository:
```bash
git remote add upstream https://github.com/bob-crutchley/notes
```
2. Fetch the remote branches from the new upstream:
```bash
git fetch upstream
```
3. Rewrite your master branch to accommodate for the new changes:
```bash
git rebase upstream/master
```
4. Push the changes to your repository:
```bash
git push -u origin master
```
If you are having issues pushing to your master branch, you may need to add the `--force` option to the previous command and try it again.
### Contributing
Please see the [contributing guidelines](./CONTRIBUTING.md).
### Automation
Links to topic modules are included on main topic README files and a table of contents is entered into every README file.
This has been automated by Python scripts in the `automation` folder:
- `modules.py` - Generate module links for the main README on topics
- `toc.py` - Generate a table of contents for every README on the project
#### Circle CI
Circle CI has been setup to run these scripts automatically and then commit the changes back to the branch being built, so don't feel like you need to get these scripts working before making a pull request.
#### Local Setup
You'll need to install some dependencies from the `pip_dependecies` files; using a virtual environment is also recommended.
1. Make sure you have Python 3.* installed, as well as Pip
2. Make sure virtualenv is installed with `pip install virtualenv`
3. Configure a virtual environment with `virtualenv -p python3 venv` 
4. Load into the virtual environment: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r pip_dependecies`
