{ 
  # create hello.yaml file
  # enable .gitignore creation
  config.files.gitignore.enable = true;
  # add hello.yaml to .gitignore
  # copy contents from https://github.com/github/gitignore
  # to our .gitignore
  config.files.gitignore.template."Global/Archives" = true;
  config.files.gitignore.template."Global/Backup" = true;
  config.files.gitignore.template."Global/Diff" = true;
  config.files.gitignore.template."Python" = true;
  # now we can use 'convco' command https://convco.github.io
  config.files.cmds.convco = true;
  # now we can use 'featw' command as alias to convco
  config.files.alias.feat = ''convco commit --feat $@'';
  config.files.alias.fix = ''convco commit --fix $@'';
  config.files.alias.chore = ''convco commit --chore $@'';

  config.files.cmds.python39 = true;
  config.files.cmds.awscli = true;
  config.files.cmds.pipenv = true;
  config.files.cmds.yj = true;
  config.files.cmds.nodejs-16_x = true;
}
