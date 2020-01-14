from ariadne import QueryType, gql, make_executable_schema

from graph.githubApi import call_repos_by_user, call_detail_by_repo

type_defs = gql("""
    type Query {
        repos(user: String): [Repo]
        repo(user: String!, repo: String!) : Repo!
    }

    type Repo    {
        id: String!
        node_id: String!
        name: String!
        full_name: String!
        private: Boolean!
        description: String
    }

""")

query = QueryType()


@query.field("repos")
def resolve_repos(*_, user):
    return call_repos_by_user(user)


@query.field("repo")
def resolve_repo(*_, user, repo):
    return call_detail_by_repo(user, repo)


schema = make_executable_schema(type_defs, query)

