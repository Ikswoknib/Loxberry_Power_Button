#!/usr/bin/perl

use LoxBerry::Web;
my $plugintitle = "LoxBerry Powerbutton" . LoxBerry::System::pluginversion();
#my $helplink = "";
#my $helptemplate = "";

LoxBerry::Web::lbheader($plugintitle, $helplink, $helptemplate);

my $template = HTML::Template->new(
    filename => "$lbptemplatedir/index.html",
    global_vars => 1,
    loop_context_vars => 1,
    die_on_bad_params => 0,
);

print $template->output();

LoxBerry::Web::lbfooter();
