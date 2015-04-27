#!/usr/bin/env rspec

describe 'bugs' do
  it 'should be no untriaged bugs older then one week'
  it 'should be no unassigned critical bugs'
  it 'should be no bugs in progress for more then two weeks without action'
  it 'should be no triaged bugs without assignee, priority, milestone'
  it 'should be no bugs in progress without assignee or with assigned team'
  it 'should be no bugs in incomplete state with response and no action for a week'
  it 'should be no bugs in incomplete state without an action for a month'
end

describe 'blueprints' do
  it 'should be no blueprints without series'
  it 'should be no open blueprints without a milestone'
  it 'should be no rejected blueprints with a milestone'
  it 'should be no implemented blueprints without approved direction or definition'
  it 'should be no started blueprints without assignee'
  it 'should be no blueprints without priority'
end

describe 'milestones and series' do
  it 'should be no closed milestones with open bugs or blueprints'
  it 'should be no series with bugs or blueprints on milestones from other series'
end

describe 'reviews' do
  it 'should be no open reviews without reviewers'
  it 'should be no open reviews created more then three monthes ago'
  it 'should be no reviews without an action for a week and without wip flag'
  it 'should be no reviews without an action for a month'
  it 'should be no merged reviews without two approvals'
end
