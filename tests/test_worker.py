from main import WikiClient, PlosClient, Woker


def test_worker(monkeypatch):
    execute_cnt = 0
    executed_urls = set()

    def mock_make_get_request(*args, **kwargs):
        nonlocal execute_cnt
        nonlocal executed_urls
        execute_cnt += 1
        executed_urls.add(args[0].base_url)

    monkeypatch.setattr("main.ConcreteBaseClient.make_get_request", mock_make_get_request)

    wiki_url = "https://test_url_wiki"
    plos_url = "http://test_url_plos"

    wiki_client = WikiClient(wiki_url)
    plos_client = PlosClient(plos_url)
    worker = Woker(wiki_client, plos_client)
    worker()
    assert execute_cnt == 2
    assert {wiki_url, plos_url} == executed_urls
