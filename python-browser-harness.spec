Name:		python-browser-harness
Version:	0.1.13
Release:	1
Summary:	Control a local browser through the Chrome DevTools Protocol
License:	MIT
Group:		Development/Python
URL:		https://github.com/browser-use/browser-harness
Source0:	https://files.pythonhosted.org/packages/source/b/browser-harness/browser_harness-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
browser-harness connects an agent to a local Chrome or Chromium
through one DevTools websocket. Hermes uses it as the browser_exec
engine. The optional MCP extra is not packaged; browser-harness-mcp
explains that when the mcp module is missing.

Upstream pins Pillow 12.3.0 and websockets 15.0.1. Cooker has Pillow
13 and websockets 17, which provide the APIs this package calls, so
the pins are widened.

%prep -a
rm -rf src/browser_harness.egg-info
sed -i \
	-e 's/cdp-use==1.4.5/cdp-use>=1.4.5/' \
	-e 's/fetch-use==0.4.0/fetch-use>=0.4.0/' \
	-e 's/pillow==12.3.0/pillow>=11.1.0/' \
	-e 's/websockets==15.0.1/websockets>=15/' \
	pyproject.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/browser-harness
%{_bindir}/browser-harness-mcp
%{python_sitelib}/browser_harness
%{python_sitelib}/mcp_server.py
%{python_sitelib}/__pycache__/mcp_server.cpython-*.pyc
%{python_sitelib}/browser_harness-%{version}.dist-info
